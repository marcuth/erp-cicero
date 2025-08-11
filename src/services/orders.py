from sqlalchemy.exc import IntegrityError, NoResultFound
from datetime import date, timedelta

from enums.installment_status import InstallmentStatus
from models.installment import Installment
from enums.payment_type import PaymentType
from enums.payment_type import PaymentType
from models.order_item import OrderItem
from models.product import Product
from models.order import Order
from db import SessionLocal

def create_order(
    seller_id: int,
    customer_id: int,
    items: list[dict],
    payment_type: PaymentType,
    installments: int = 1
) -> Order:
    session = SessionLocal()
    
    try:
        product_ids = [i["product_id"] for i in items]
        products = {p.id: p for p in session.query(Product).filter(Product.id.in_(product_ids)).all()}

        if len(products) != len(product_ids):
            raise ValueError("Um ou mais produtos não encontrados")

        total_price = 0
        
        order = Order(
            seller_id=seller_id,
            customer_id=customer_id,
            payment_type=payment_type,
            total_price=0
        )
        
        session.add(order)
        session.flush()

        for item in items:
            product = products[item["product_id"]]
            quantity = item["quantity"]

            if product.stock < quantity:
                raise ValueError(f"Estoque insuficiente para {product.name}")

            product.stock -= quantity
            subtotal = product.sell_price * quantity
            total_price += subtotal
            
            order_item = OrderItem(
                order_id=order.id,
                product_id=product.id,
                quantity=quantity,
                unit_price=product.sell_price
            )

            session.add(order_item)

        order.total_price = total_price

        if payment_type == PaymentType.INSTALLMENTS:
            if installments < 1:
                raise ValueError("Parcelamento precisa ter pelo menos 1 parcela")
            
            now = date.today()
            
            for i in range(installments):
                installment = Installment(
                    order_id=order.id,
                    seller_id=seller_id,
                    customer_id=customer_id,
                    must_be_paid_at=now + timedelta(days=30 * (i + 1)),
                    status=InstallmentStatus.PENDING,
                    paid_at=None
                )
                
                session.add(installment)

        elif payment_type == PaymentType.CASH:
            installment = Installment(
                order_id=order.id,
                seller_id=seller_id,
                customer_id=customer_id,
                must_be_paid_at=date.today(),
                paid_at=date.today(),
                status=InstallmentStatus.PAID
            )
            
            session.add(installment)

        session.commit()
        
        return order

    except IntegrityError:
        session.rollback()
        raise ValueError("Erro ao criar pedido")
    
    except Exception as e:
        session.rollback()
        raise e
    
    finally:
        session.close()


def find_all_orders() -> list[Order]:
    session = SessionLocal()
    
    try:
        return session.query(Order).all()
    finally:
        session.close()


def find_first_order(**filters) -> Order | None:
    session = SessionLocal()
    
    try:
        query = session.query(Order)
        for field, value in filters.items():
            if hasattr(Order, field):
                query = query.filter(getattr(Order, field) == value)
        return query.first()
    
    finally:
        session.close()


def delete_order(order_id: int) -> bool:
    session = SessionLocal()
    
    try:
        order = session.query(Order).filter(Order.id == order_id).one()
        session.delete(order)
        session.commit()
        return True
    
    except NoResultFound:
        session.rollback()
        raise ValueError("Pedido não encontrado")
    
    finally:
        session.close()
