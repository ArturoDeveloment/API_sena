from typing import TYPE_CHECKING

from db import database

# DONT DELETE!!!!!!!!!!!!!!!!!!!!!!!!!!!

from models import formation_area_model
from models import program_model
from schemas import formation_area_schema
from schemas import program_schema

# IMPORTANT!!!!!!!!!!!!!!!!!!!!!!!!!!!!

if TYPE_CHECKING:
    from sqlalchemy.orm import Session


def create_tables():
    return database.Base.metadata.create_all(bind=database.engine)


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()
