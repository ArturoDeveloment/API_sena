import datetime as _dt
import sqlalchemy as _sql

from db import database


class FormationArea(database.Base):
    __tablename__: str = "formation_areas"
    id: int = _sql.Column(_sql.Integer, primary_key=True, index=True)
    name: str = _sql.Column(_sql.String(100), index=True)
    description: str = _sql.Column(_sql.String(500), index=True)
    status: str = _sql.Column(
        _sql.Enum("active", "inactive", name="formation_area_status"),
        index=True,
        default='active'
    )
    created_at: _dt.datetime = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    updated_at: _dt.datetime = _sql.Column(
        _sql.DateTime, default=_dt.datetime.utcnow, onupdate=_dt.datetime.utcnow
    )