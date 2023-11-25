import os

from data.database import Database
from modules.helpers import check_password
from modules.pdf_processor import pdf_processor
from modules.chat_chain import chat_chain
import modules.globals as globals

# Commands and their default values
# None is used when default value not needed
# These commands can be input at any point the user is prompted
commands = [
    {"command": "-dir", "default_value": "./samples", "description": "pdf files directory"},
    {"command": "-p", "default_value": None, "description": "process updated pdf files"},
    {"command": "-chat", "default_value": None, "description": "enter chat mode"},
    {"command": ["-quit", "-q"], "default_value": None, "description": "quit app or chat mode"},
    {"command": ["-help", "-h"], "default_value": None, "description": "show help message"},
    {"command": "-u", "default_value": None, "description": "username"},
    {"command": "-p", "default_value": None, "description": "password"},
    {"command": "-n", "default_value": None, "description": "create new user ex. -u (new_username) -p (pasword) -r (admin or user)"},
    {"command": "-o", "default_value": None, "description": "logout"},
    {"command": "-r", "default_value": None, "description": "role used with -u and -p"},
    {"command": "-d", "default_value": None, "description": "update user role -u, -p, and -r"},
    {"command": "-i", "default_value": None, "description": "update custom instructions ex. -i (custom instructions)"},
    {"command": "-f", "default_value": None, "description": "create user feedback"},
]

class UserHandler:
    def __init__(self, db: Database, processor: pdf_processor, chain: chat_chain):
        self._database = db
        self._pdf_processor = processor
        self._chain = chain

    def show_help(self):
        for cmd in commands:
            if cmd["default_value"] is not None:
                print(f"\t{cmd['command']} (default: {cmd['default_value']}) {cmd['description']}")
            else:
                print(f"\t{cmd['command']} {cmd['description']}")

    def show_login(self):
        while True:
            login = input("\nLogin: ")
            parts = login.split()

            if "-h" in parts:
                self.show_help()

            username, password, role = self.parse_user_info(parts)

            if username is not None and password is not None:
                user = self._database.get_user(username)

                if user is None:
                    print("\tUser does not exist.")    
                elif not check_password(password, user.password):
                    print("\tWrong password.")
                else:
                    return user
            else:
                print("\tInvalid login format. Please provide both username and password.")

    def parse_user_info(self, parts):
        username = None
        password = None
        role = None
        
        for i, part in enumerate(parts):
                if part == "-u" and i < len(parts) - 1:
                    username = parts[i + 1]
                elif part == "-p" and i < len(parts) - 1:
                    password = parts[i + 1]
                elif part == "-r" and i < len(parts) - 1:
                    role = parts[i + 1]

        return username, password, role

    def handle_dir_update(self, parts):
        directory = self.parse_dir(parts)

        if directory is not None:
            globals.pdf_files_dir = directory
            self._pdf_processor.process(directory)

    def parse_dir(self, parts):
        try:
            dir_index = parts.index("-dir") + 1

            if dir_index < len(parts):
                directory = parts[dir_index]

                if os.path.exists(directory) and os.path.isdir(directory):
                    pdf_files = [file for file in os.listdir(directory) if file.endswith(".pdf")]

                    if pdf_files:
                        print(f"\tSwitched to {directory} directory. Found {len(pdf_files)} PDF files.")
                        return directory
                    else:
                        print(f"\t Directory verified, but there are no PDF files.")
                else:
                    print(f"\tThe directory '{directory}' does not exist or is not a valid directory.")
            else:
                print("\tPlease provide a directory path after -dir.")
        except ValueError:
            print("Invalid command format. Use -dir to specify a directory.")

    def handle_new_user(self, parts):
        username, password, role = self.parse_user_info(parts)
        
        if username and password:
            new_user = self._database.create_user(username, password, role)
            print("Successfully created new user.")
            return new_user
        else:
            print("Invalid command format. Use -n with -u, -p, and -r.")

    def handle_user_update(self, parts):
        username, password, role = self.parse_user_info(parts)
        
        if username and password:
            new_user = self._database.update_user(username, password, role)
            print("Successfully created new user.")
            return new_user
        else:
            print("Invalid command format. Use -n with -u, -p, and -r.")

    def handle_update_custom_instructions(self, username, parts):
        custom_instruction = None
        for i, part in enumerate(parts):
            if part == "-i" and i < len(parts) - 1:
                custom_instruction = parts[i + 1]

        if custom_instruction:
            self._database.update_custom_instruction(username, custom_instruction)
        else:
            print("Invalid command format. Add new custom instruction after -i.")

    def handle_user_feedback(self, user_id, parts):
        user_feedback = None
        for i, part in enumerate(parts):
            if part == "-i" and i < len(parts) - 1:
                user_feedback = parts[i + 1]

        if user_feedback:
            self._database.create_user_feedback(user_id, user_feedback)
        else:
            print("Invalid command format. Add new feedback after -f.")

    def init(self):
        while True:
            print(f"Welcome to PDF Query Tool")

            self.show_help()
            user = self.show_login()
            is_admin = user.role.name == 'admin'

            while True:
                user_input = input(f"\nWhat would you like to do {user.username}? ")
                parts = user_input.split()

                if "-q" in parts or "-quit" in parts:
                    return
                elif "-o" in parts:
                    break
                elif "-help" in parts or "-h" in parts:
                    self.show_help()
                    continue

                if is_admin:
                    if "-n" in parts:
                        self.handle_new_user(parts)

                    if "-d" in parts:
                        self.handle_user_update(parts)

                    if "-dir" in parts:
                        self.handle_dir_update(parts)
                        self._pdf_processor.process(globals.pdf_files_dir)

                    if "-p" in parts:
                        self._pdf_processor.process(globals.pdf_files_dir)

                if "-i" in parts:
                    self.handle_update_custom_instructions(user.username, parts)

                if "-f" in parts:
                    self.handle_user_feedback(user.user_id, parts)

                if "-chat" in parts:
                    while True:
                        query = input(f"\n?: ")
                        
                        if "-q" in query or "-quit" in query:
                            break

                        self._chain.new_query(query)