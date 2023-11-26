# import typing as t

# from datetime import datetime

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from . import crud, models, schema
from .database import SessionLocal, Engine

models.SqlBaseModel.metadata.create_all(bind=Engine)

# FastAPI object initialization
app = FastAPI(
    description="This is the backend project for inventory management "
    "using FastAPI for API development"
)

# adding cors middleware to allow cross-origin request that can come from
# different protocol, domains or ports
# reference: https://fastapi.tiangolo.com/tutorial/cors/#cors-cross-origin-resource-sharing # noqa
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database Session is created and then terminated when the request
# is completed.


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root_path():
    return "This is the root path of Inventory Management framework"


@app.post("/users/", response_model=schema.User)
def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/{user_id}", response_model=schema.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=400, detail="User not found")
    return db_user


@app.get("/users/", response_model=list[schema.User])
def get_all_users(skip: int = 0, limit: int = 100,
                  db: Session = Depends(get_db)):
    db_users = crud.get_users(db=db, skip=skip, limit=limit)
    return db_users


@app.post("/items/", response_model=schema.Item)
def create_user_item(user_id: int, item: schema.ItemCreate,
                     db: Session = Depends(get_db)):
    db_user_item = crud.create_user_item(db=db, item=item, user_id=user_id)
    return db_user_item


@app.get("/items/", response_model=list[schema.Item])
def get_all_items(skip: int = 0, limit: int = 100,
                  db: Session = Depends(get_db)):
    db_items = crud.get_items(db=db, skip=skip, limit=limit)
    return db_items
