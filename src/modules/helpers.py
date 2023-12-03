from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
import bcrypt

from data.models import User, Role, UserFeedback, UploadedDoc

def get_hashed_password(plain_text_password):
    bytes = plain_text_password.encode('utf-8')
    return bcrypt.hashpw(bytes, bcrypt.gensalt())

def check_password(plain_text_password, hashed_password):
    bytes = plain_text_password.encode('utf-8')
    return bcrypt.checkpw(bytes, hashed_password)

class RoleSchema(SQLAlchemySchema):
    class Meta:
        model = Role
        include_fk = True
        include_relationships = True

    role_id = auto_field()
    name = auto_field()
    role_users = auto_field()


class UserSchema(SQLAlchemySchema):
    class Meta:
        model = User
        include_fk = True
        include_relationships = True

    user_id = auto_field()
    username = auto_field()
    password = auto_field()
    created_date = auto_field()
    custom_instruction = auto_field()
    last_chat = auto_field()
    user_role_id = auto_field()
    user_role = auto_field()
    feedbacks = auto_field()
    documents = auto_field()

class UserFeedbackSchema(SQLAlchemySchema):
    class Meta:
        model = UserFeedback
        include_fk = True
        include_relationships = True

    user_feedback_id = auto_field()
    created_date = auto_field()
    feedback = auto_field()
    is_archived = auto_field()
    owner_id = auto_field()
    owner = auto_field()

class UploadedDocSchema(SQLAlchemySchema):
    class Meta:
        model = UploadedDoc
        include_fk = True
        include_relationships = True

    uploaded_doc_id = auto_field()
    name = auto_field()
    created_date = auto_field()
    uploader_id = auto_field()
    uploader = auto_field()