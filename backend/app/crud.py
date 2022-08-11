from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException
from . import models, schemas


def get_author(db: Session, author_id: int):
    return db.query(models.Author).filter(models.Author.id == author_id).first()


def get_authors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Author).offset(skip).limit(limit).all()


def create_author(db: Session, author: schemas.AuthorCreate):
    db_author = models.Author(name=author.name)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author
def update_author(db: Session,author_id:int, author: schemas.AuthorCreate):
    db_author =  db.query(models.Author).get(author_id)
    if not db_author:
            raise HTTPException(status_code=404, detail="Author not found")
    author_data = author.dict(exclude_unset=True)
    for key, value in author_data.items():
            setattr(db_author, key, value)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

def delete_author(db: Session,author_id:int):
    db_author =  db.query(models.Author).get(author_id)
    if not db_author:
            raise HTTPException(status_code=404, detail="Author not found")
    db.delete(db_author)
    db.commit()
    return { "ok" : True}



def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Book).offset(skip).limit(limit).all()


def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book
def update_book(db: Session,book_id:int, book: schemas.BookCreate):
    db_book =  db.query(models.Book).get(book_id)
    if not db_book:
            raise HTTPException(status_code=404, detail="book not found")
    book_data = book.dict(exclude_unset=True)
    for key, value in book_data.items():
            setattr(db_book, key, value)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def delete_book(db: Session,book_id:int):
    db_book =  db.query(models.Book).get(book_id)
    if not db_book:
            raise HTTPException(status_code=404, detail="book not found")
    db.delete(db_book)
    db.commit()
    return { "ok" : True}




def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Category).offset(skip).limit(limit).all()


def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = models.Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def update_category(db: Session,category_id:int, category: schemas.CategoryCreate):
    db_category =  db.query(models.Category).get(category_id)
    if not db_category:
            raise HTTPException(status_code=404, detail="Category not found")
    category_data = category.dict(exclude_unset=True)
    for key, value in category_data.items():
            setattr(db_category, key, value)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def delete_category(db: Session,category_id:int):
    db_category =  db.query(models.Category).get(category_id)
    if not db_category:
            raise HTTPException(status_code=404, detail="Category not found")
    db.delete(db_category)
    db.commit()
    return { "ok" : True}