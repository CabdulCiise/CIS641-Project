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
            'user_role_id': 1
        },
        {
            'first_name': 'User',
            'last_name': 'Test',
            'username': 'user',
            'password': get_hashed_password('user'),
            'user_role_id': 2
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
        self._connection = self._engine.connect()

    def setup_seeding_events(self):
        event.listen(Role.__table__, 'after_create', initialize_table)
        event.listen(User.__table__, 'after_create', initialize_table)

    def init(self):
        self.setup_seeding_events()
        Base.metadata.create_all(bind=self._engine)

    def get_user(self, username):
        stmt = select(User).where(User.username == username)

        return self._connection.execute(statement=stmt).fetchone()
    
    def get_users(self):
        stmt = select(User)

        return self._connection.execute(statement=stmt).fetchall()
    
    def create_user(self, username, password, role="user"):
        user = self.get_user(username)
        added_user = None
        
        if not user:
            stmt = insert(User).values(
                username=username,
                password=get_hashed_password(password),
                user_role_id=1 if role == "admin" else 2
            ).returning(User)

            added_user = self._connection.execute(statement=stmt).fetchone()
            self._connection.commit()
        else:
            return added_user, "Username is not available."

        return added_user, None
    
    def update_user(self, user_id, role):
        session = Session(self._engine)
        stmt = update(User).where(User.user_id == user_id).values(
            role_id=1 if role == "admin" else 2,
        ).returning(User)

        updated_user = session.scalar(statement=stmt)
        session.commit()
        return updated_user
    
    def update_custom_instruction(self, user_id, custom_instruction):
        stmt = update(User).where(User.user_id == user_id).values(
            custom_instruction=custom_instruction
        ).returning(User)

        updated_user = self._connection.execute(statement=stmt).fetchone()
        self._connection.commit()
        return updated_user
    
    def get_roles(self):
        session = Session(self._engine)
        stmt = select(Role)

        return session.scalars(statement=stmt).all()
    
    def get_user_feedbacks(self, only_archived=False):
        stmt = select(UserFeedback).where(UserFeedback.is_archived == only_archived).order_by(UserFeedback.created_date.desc())

        return self._connection.execute(statement=stmt).fetchall()

    def create_user_feedback(self, user_id, feedback):
        stmt = insert(UserFeedback).values(
            owner_id=user_id,
            is_archived=False,
            feedback=feedback,
        ).returning(UserFeedback)

        added_feedback = self._connection.execute(statement=stmt).fetchone()
        self._connection.commit()
        return added_feedback
    
    def update_user_feedback(self, user_feedback_id, is_archived):
        session = Session(self._engine)
        stmt = update(UserFeedback).where(UserFeedback.user_feedback_id == user_feedback_id).values(
            is_archived=is_archived
        ).returning(UserFeedback)

        updated_feedback = self._connection.execute(statement=stmt).fetchone()
        self._connection.commit()
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
