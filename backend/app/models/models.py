from sqlalchemy import  Column, ForeignKey, Integer, String , DateTime
from sqlalchemy.sql import func
from ..db import Base

class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    created_at  = Column(DateTime, default=func.now())
    updated_at  = Column(DateTime, default=func.now(),onupdate=func.current_timestamp())

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    price = Column(Integer)
    author_id = Column(Integer, ForeignKey("authors.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))
    created_at  = Column(DateTime, default=func.now())
    updated_at  = Column(DateTime, default=func.now(),onupdate=func.current_timestamp())

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    created_at  = Column(DateTime, default=func.now())
    updated_at  = Column(DateTime, default=func.now(),onupdate=func.current_timestamp())