import datetime as _dt
import sqlalchemy as _sql

from db import database


class SubOffice(database.Base):
    __tablename__: str = "sub_offices"
    id: int = _sql.Column(_sql.Integer, primary_key=True, index=True)
    name: str = _sql.Column(_sql.String(100), index=True)
    description: str = _sql.Column(_sql.String(500), index=True)
    partners: str = _sql.Column(_sql.String(500), index=True)
    status: str = _sql.Column(
        _sql.Enum("active", "inactive", name="sub_office_status"),
        index=True,
        default='active'
    )

    office_id: int = _sql.Column(_sql.Integer, _sql.ForeignKey('offices.id'))

    created_at: _dt.datetime = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    updated_at: _dt.datetime = _sql.Column(
        _sql.DateTime, default=_dt.datetime.utcnow, onupdate=_dt.datetime.utcnow
    )