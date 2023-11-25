import bcrypt

def get_hashed_password(plain_text_password):
    bytes = plain_text_password.encode('utf-8')
    return bcrypt.hashpw(bytes, bcrypt.gensalt())

def check_password(plain_text_password, hashed_password):
    bytes = plain_text_password.encode('utf-8')
    return bcrypt.checkpw(bytes, hashed_password)