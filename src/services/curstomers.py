from sqlalchemy.exc import IntegrityError, NoResultFound

from models.customer import Customer
from enums.gender import Gender
from db import SessionLocal

def create_customer(
    name: str,
    cpf: str,
    state: str,
    city: str,
    address: str,
    phone: str,
    email: str,
    gender: Gender
):
    session = SessionLocal()
    
    try:
        customer = Customer(
            name=name,
            cpf=cpf,
            state=state,
            city=city,
            address=address,
            phone=phone,
            email=email,
            gender=gender
        )
        
        session.add(customer)
        session.commit()
        
        return customer
    
    except IntegrityError:
        session.rollback()
        raise ValueError("Erro ao criar cliente — verifique CPF único ou dados obrigatórios")
    
    finally:
        session.close()


def update_customer(customer_id, **kwargs):
    session = SessionLocal()
    
    try:
        customer = session.query(Customer).filter(Customer.id == customer_id).one()

        for field, value in kwargs.items():
            if hasattr(Customer, field):
                setattr(customer, field, value)

        session.commit()
        
        return customer
    
    except NoResultFound:
        session.rollback()
        raise ValueError("Cliente não encontrado")
    
    except IntegrityError:
        session.rollback()
        raise ValueError("Erro de integridade ao atualizar cliente")
    
    finally:
        session.close()

def delete_customer(customer_id):
    session = SessionLocal()
    
    try:
        customer = session.query(Customer).filter(Customer.id == customer_id).one()
        session.delete(customer)
        session.commit()
        return True
    
    except NoResultFound:
        session.rollback()
        raise ValueError("Cliente não encontrado")
    
    finally:
        session.close()

def find_all_customers():
    session = SessionLocal()
    
    try:
        return session.query(Customer).all()
    finally:
        session.close()

def find_first_customer(**filters):
    session = SessionLocal()
    
    try:
        query = session.query(Customer)
        
        for field, value in filters.items():
            if hasattr(Customer, field):
                query = query.filter(getattr(Customer, field) == value)
                
        return query.first()
    
    finally:
        session.close()
