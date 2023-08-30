import datetime as _dt
import sqlalchemy as _sql
from pydantic import BaseModel

from db import database

class User(BaseModel):
    id: int
    user_name: str
    password: str
    token: str

class UserModel(database.Base):
    __tablename__ = 'users'
    id: int = _sql.Column(_sql.Integer, primary_key=True, index=True)
    user_name: str = _sql.Column(_sql.String(100), index=True)
    password: str = _sql.Column(_sql.String(100), index=True)
    token: str = _sql.Column(_sql.String(100), index=True)
    created_at: _dt.datetime = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    updated_at: _dt.datetime = _sql.Column(
        _sql.DateTime, default=_dt.datetime.utcnow, onupdate=_dt.datetime.utcnow
    )