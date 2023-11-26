from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# references:
# sqlalchemy: https://www.sqlalchemy.org/
# sql database: https://fastapi.tiangolo.com/tutorial/sql-databases/#sql-relational-databases # noqa


SQLALCHEMY_DATABASE_URL = "sqlite:///./inventory_app.db"

Engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=Engine)

SqlBaseModel = declarative_base()
