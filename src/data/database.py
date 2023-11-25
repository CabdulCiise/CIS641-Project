from data.models import Base, Role, User, UserFeedback, UploadedDoc
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
        stmt = insert(User).values(
            username=username,
            password=get_hashed_password(password),
            role_id=1 if role == "admin" else 2
        ).returning(User)

        added_user = session.scalar(statement=stmt)
        session.commit()
        return added_user
    
    def update_user(self, username, password, role):
        session = Session(self._engine)
        stmt = update(User).where(User.username == username).values(
            password=get_hashed_password(password),
            role_id=1 if role == "admin" else 2
        ).returning(User)

        updated_user = session.scalar(statement=stmt)
        session.commit()
        return updated_user
    
    def update_user_custom_instruction(self, username, custom_instruction):
        session = Session(self._engine)
        stmt = update(User).where(User.username == username).values(
            custom_instruction=custom_instruction
        ).returning(User)

        updated_user = session.scalar(statement=stmt)
        session.commit()
        return updated_user
    
    def get_user_feedbacks(self, include_archived=False):
        session = Session(self._engine)
        stmt = select(UserFeedback)
        
        if not include_archived:
            stmt = stmt.where(UserFeedback.is_archived == False)

        return session.scalars(statement=stmt)

    def create_user_feedback(self, user_id, feedback):
        session = Session(self._engine)
        stmt = insert(UserFeedback).values(
            user_id=user_id,
            is_archived=False,
            feedback=feedback,
        ).returning(UserFeedback)

        added_feedback = session.scalar(statement=stmt)
        session.commit()
        return added_feedback
    
    def update_user_feedback(self, user_feedback_id, is_archived):
        session = Session(self._engine)
        stmt = update(UserFeedback).where(UserFeedback.user_feedback_id == user_feedback_id).values(
            is_archived=is_archived
        ).returning(UserFeedback)

        updated_feedback = session.scalar(statement=stmt)
        session.commit()
        return updated_feedback
    
    def create_uploaded_doc(self, user_id, file_name):
        session = Session(self._engine)
        stmt = insert(UploadedDoc).values(
            user_id=user_id,
            name=file_name,
        ).returning(UploadedDoc)

        added_file = session.scalar(statement=stmt)
        session.commit()
        return added_file
    
    def delete_uploaded_doc(self, file_name):
        session = Session(self._engine)
        stmt = delete(UploadedDoc).where(UploadedDoc.name == file_name)

        session.execute(statement=stmt)
        session.commit()
    
    def get_uploaded_docs(self):
        session = Session(self._engine)
        stmt = select(UploadedDoc)
        return session.scalars(statement=stmt)
