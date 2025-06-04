from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("items.item_id"))
    user_id = Column(Integer, ForeignKey("users.user_id"))
    
    item = relationship("Item")
    user = relationship("User")