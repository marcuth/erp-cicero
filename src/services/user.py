from sqlalchemy.exc import IntegrityError

from utils.security import hash_password
from models.user import User
from db import SessionLocal

def create_user(username, name, role, password):
    session = SessionLocal()
    
    try:
        user = User(
            username=username,
            name=name,
            role=role,
            password=hash_password(password)
        )
        
        session.add(user)
        session.commit()
        
        return user
    
    except IntegrityError:
        session.rollback()
        raise ValueError("Username já existe")
    
    finally:
        session.close()