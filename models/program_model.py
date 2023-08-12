import datetime as _dt
import sqlalchemy as _sql

from db import database


class Program(database.Base):
    __tablename__: str = "programs"
    id: int = _sql.Column(_sql.Integer, primary_key=True, index=True)
    name: str = _sql.Column(_sql.String(100), index=True)
    description: str = _sql.Column(_sql.String(500), index=True)
    level: str = _sql.Column(
        _sql.Enum(
            "technical",
            "technologist",
            "operator",
            "specialization",
            "assistant",
            name="program_level",
        ),
        index=True,
    )
    term: str = _sql.Column(_sql.String(100), index=True)
    journies: str = _sql.Column(
        _sql.Enum("morning", "afternoon", "night", name="program_journies"),
        index=True,
    )
    status: str = _sql.Column(
        _sql.Enum("active", "inactive", name="program_status"),
        index=True,
        default='active'
    )

    formation_area_id: int = _sql.Column(_sql.Integer, _sql.ForeignKey('formation_areas.id'))

    created_at: _dt.datetime = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    updated_at: _dt.datetime = _sql.Column(
        _sql.DateTime, default=_dt.datetime.utcnow, onupdate=_dt.datetime.utcnow
    )