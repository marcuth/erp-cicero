from sqlalchemy.exc import IntegrityError, NoResultFound
from typing import Optional

from utils.security import hash_password
from enums.user_role import UserRole
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
        
def update_user(
    user_id: str,
    username: Optional[str]=None,
    name: Optional[str]=None,
    role: Optional[UserRole]=None,
    password=None
):
    session = SessionLocal()
    
    try:
        user = session.query(User).filter(User.id == user_id).one()
        
        if username is not None:
            user.username = username
            
        if name is not None:
            user.name = name
            
        if role is not None:
            user.role = role
            
        if password is not None and password.strip():
            user.password = hash_password(password)
        
        session.commit()
        
        return user
    
    except NoResultFound:
        session.rollback()
        raise ValueError("Usuário não encontrado")
    
    except IntegrityError:
        session.rollback()
        raise ValueError("Username já existe")
    
    finally:
        session.close()

def delete_user(user_id: str):
    session = SessionLocal()
    
    try:
        user = session.query(User).filter(User.id == user_id).one()
        session.delete(user)
        session.commit()
    
    except NoResultFound:
        session.rollback()
        raise ValueError("Usuário não encontrado")
    
    finally:
        session.close()
        
def find_all_users():
    session = SessionLocal()
    
    try:
        return session.query(User).all()
    finally:
        session.close()

def find_first_customers(**filters):
    session = SessionLocal()
    
    try:
        query = session.query(User)
        
        for field, value in filters.items():
            if hasattr(User, field):
                query = query.filter(getattr(User, field) == value)
                
        return query.first()
    
    finally:
        session.close()