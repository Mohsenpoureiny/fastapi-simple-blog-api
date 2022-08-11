from datetime import datetime
from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    price: int
    author_id: int
    category_id: int


class BookCreate(BookBase):
    title: str
    price: int
    author_id: int
    category_id: int


class Book(BookBase):
    id: int
    title: str
    price: int
    author_id: int
    category_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class AuthorBase(BaseModel):
    name: str


class AuthorCreate(AuthorBase):
    name: str


class Author(AuthorBase):
    id: int
    name: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class Category(BaseModel):
    id: int
    name: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class CategoryBase(BaseModel):
    name: str



class CategoryCreate(BaseModel):
    name: str