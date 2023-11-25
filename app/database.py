from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# references:
# sqlalchemy: https://www.sqlalchemy.org/
# sql database: https://fastapi.tiangolo.com/tutorial/sql-databases/#sql-relational-databases


SQLALCHEMY_DATABASE_URL = "sqlite:///./inventory_app.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = declarative_base()
