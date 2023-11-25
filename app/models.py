from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import SqlBaseModel


class User(SqlBaseModel):
    # creating table with "users" as tablename in the database
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    items = relationship("Item", back_populates="owner")


class Item(SqlBaseModel):
    # creating table with "items" as tablename in the database
    __tablename__ = "items"

    # creating various columns in the databases
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="items")
