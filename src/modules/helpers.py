from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, SQLAlchemySchema
import bcrypt

from data.models import User, Role, UserFeedback, UploadedDoc

def get_hashed_password(plain_text_password):
    bytes = plain_text_password.encode('utf-8')
    return bcrypt.hashpw(bytes, bcrypt.gensalt())

def check_password(plain_text_password, hashed_password):
    bytes = plain_text_password.encode('utf-8')
    return bcrypt.checkpw(bytes, hashed_password)

class UserFeedbackSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = UserFeedback

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User

class RoleSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Role

class UploadedDocSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = UploadedDoc