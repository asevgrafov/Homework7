from sqlalchemy import Column, create_engine, Sequence, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
import config
from OrderStatus import OrderStatus, OrderStatusInvalidStateException

Base = declarative_base()
metadata = Base.metadata


class Orders(Base):
    __tablename__ = "orders"

    id = Column(
        VARCHAR,
        Sequence('orders_id_seq'),
        primary_key=True,
        unique=True,
        comment="Идентификатор",
    )
    status = Column(
        VARCHAR,
        nullable=False,
        comment="статус заказа"
    )

    def set_status(self, status: str) -> None:
        order_status = OrderStatus(self.status)
        order_status.change_to_state(status)
        self.status = order_status.status

    def check_state(self) -> None:
        if self.status != "done":
            raise OrderStatusInvalidStateException(message="Невозможно изменить данные в текущем статусе заказа")


engine = create_engine(config.ENGINE_STRING)
Base.metadata.create_all(engine)
del engine


