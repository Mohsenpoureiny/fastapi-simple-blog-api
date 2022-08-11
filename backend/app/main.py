from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .db import SessionLocal, engine , init_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
async def startup_event():
    init_db()


# Author api
@app.post("/author/", response_model=schemas.Author)
def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    return crud.create_author(db=db, author=author)


@app.get("/author/", response_model=List[schemas.Author])
def read_authors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    author = crud.get_authors(db, skip=skip, limit=limit)
    return author


@app.get("/author/{author_id}", response_model=schemas.Author)
def read_author(author_id: int, db: Session = Depends(get_db)):
    db_author = crud.get_author(db, author_id=author_id)
    if db_author is None:
        raise HTTPException(status_code=404, detail="author not found")
    return db_author

@app.patch("/author/", response_model=schemas.Author)
def update_author(
    author_id:int,author: schemas.AuthorCreate, db: Session = Depends(get_db)
):
    return crud.update_author(db=db,author_id=author_id,author=author)

@app.delete("/author/")
def delete_author(
    author_id:int, db: Session = Depends(get_db)
):
    return crud.delete_author(db=db,author_id=author_id)


# book api

@app.post("/books/", response_model=schemas.Book)
def create_book_for_author(
    book: schemas.BookCreate, db: Session = Depends(get_db)
):
    return crud.create_book(db=db, book=book)


@app.get("/books/", response_model=List[schemas.Book])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    books = crud.get_books(db, skip=skip, limit=limit)
    return books

@app.patch("/books/", response_model=schemas.Book)
def update_book(
    book_id:int,book: schemas.BookCreate, db: Session = Depends(get_db)
):
    return crud.update_book(db=db,book_id=book_id,book=book)

@app.delete("/books/")
def delete_book(
    book_id:int, db: Session = Depends(get_db)
):
    return crud.delete_book(db=db,book_id=book_id)

# Category api

@app.post("/categories/", response_model=schemas.Category)
def create_category(
    category: schemas.CategoryCreate, db: Session = Depends(get_db)
):
    return crud.create_category(db=db,category=category)

@app.patch("/categories/", response_model=schemas.Category)
def update_category(
    category_id:int,category: schemas.CategoryCreate, db: Session = Depends(get_db)
):
    return crud.update_category(db=db,category_id=category_id,category=category)

@app.get("/categories/", response_model=List[schemas.Category])
def read_categories(db: Session = Depends(get_db)):
    categories = crud.get_categories(db)
    return categories

@app.delete("/categories/")
def delete_category(
    category_id:int, db: Session = Depends(get_db)
):
    return crud.delete_category(db=db,category_id=category_id)
