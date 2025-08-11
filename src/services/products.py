from sqlalchemy.exc import IntegrityError, NoResultFound

from models.bar_code import BarCode
from models.product import Product
from db import SessionLocal

def create_product(name, buy_price=0, sell_price=0, stock=0, bar_codes=None):
    session = SessionLocal()
    
    try:
        product = Product(
            name=name,
            buy_price=buy_price,
            sell_price=sell_price,
            stock=stock
        )
        
        session.add(product)
        session.flush()

        if bar_codes:
            for code in bar_codes:
                session.add(BarCode(code=code, product_id=product.id))

        session.commit()
        
        return product
    
    except IntegrityError:
        session.rollback()
        raise ValueError("Erro ao criar produto — verifique duplicidade ou dados inválidos")
    
    finally:
        session.close()

def update_product(product_id, **kwargs):
    session = SessionLocal()
    
    try:
        product = session.query(Product).filter(Product.id == product_id).one()

        bar_codes = kwargs.pop("bar_codes", None)
        
        for field, value in kwargs.items():
            if hasattr(Product, field):
                setattr(product, field, value)

        if bar_codes is not None:
            session.query(BarCode).filter(BarCode.product_id == product_id).delete()
            
            for code in bar_codes:
                session.add(BarCode(code=code, product_id=product.id))

        session.commit()
        
        return product
    
    except NoResultFound:
        session.rollback()
        raise ValueError("Produto não encontrado")
    
    except IntegrityError:
        session.rollback()
        raise ValueError("Erro de integridade ao atualizar produto")
    
    finally:
        session.close()


def delete_product(product_id):
    session = SessionLocal()
    
    try:
        product = session.query(Product).filter(Product.id == product_id).one()
        session.delete(product)
        session.commit()
        return True
    
    except NoResultFound:
        session.rollback()
        raise ValueError("Produto não encontrado")
    
    finally:
        session.close()


def find_all_products():
    session = SessionLocal()
    
    try:
        return session.query(Product).all()
    finally:
        session.close()


def find_first_product(**filters):
    session = SessionLocal()
    
    try:
        query = session.query(Product)
        
        for field, value in filters.items():
            if hasattr(Product, field):
                query = query.filter(getattr(Product, field) == value)
            
        return query.first()
    
    finally:
        session.close()
