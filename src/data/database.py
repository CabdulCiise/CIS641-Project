from data.models import Base, Role, User
from modules.helpers import get_hashed_password
from modules.globals import pdf_files_dir

from sqlalchemy import create_engine, event, select, insert, update, delete
from sqlalchemy.orm import Session

INITIAL_DATA = {
    'role': [
        {'role_id': 1, 'name': 'admin'},
        {'role_id': 2, 'name': 'user'}
    ],
    'user': [
        {
            'first_name': 'Admin',
            'last_name': 'Test',
            'username': 'admin',
            'password': get_hashed_password('admin'),
            'role_id': 1
        },
        {
            'first_name': 'User',
            'last_name': 'Test',
            'username': 'user',
            'password': get_hashed_password('user'),
            'role_id': 2
        }
    ]
}

def initialize_table(target, connection, **kw):
    tablename = str(target)
    if tablename in INITIAL_DATA and len(INITIAL_DATA[tablename]) > 0:
        connection.execute(target.insert(), INITIAL_DATA[tablename])

class Database:
    def __init__(self, echo=False):
        self._engine = create_engine("sqlite:///data/database.sqlite3", echo=echo, future=True)
        self._engine.connect()

    def setup_seeding_events(self):
        event.listen(Role.__table__, 'after_create', initialize_table)
        event.listen(User.__table__, 'after_create', initialize_table)

    def init(self):
        self.setup_seeding_events()
        Base.metadata.create_all(bind=self._engine)

    def get_user(self, username):
        session = Session(self._engine)
        stmt = select(User).where(User.username == username)

        return session.scalar(statement=stmt)
    
    def create_user(self, username, password, role):
        session = Session(self._engine)
        stmt = insert(User).returning(User),
        {
            "username": username,
            "password": get_hashed_password(password),
            "role_id": 1 if role == "admin" else 2
        }

        return session.scalar(statement=stmt)
    
    def update_user(self, username, password, role):
        session = Session(self._engine)
        stmt = update(User).where(User.username == username).returning(User),
        {
            "password": get_hashed_password(password),
            "role_id": 1 if role == "admin" else 2
        }

        return session.scalar(statement=stmt)
    
    def update_user_custom_instruction(self, username, custom_instruction):
        session = Session(self._engine)
        stmt = update(User).where(User.username == username).returning(User),
        {
            "custom_instruction": custom_instruction
        }

        return session.scalar(statement=stmt)
    
