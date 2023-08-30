import datetime as _dt
import pydantic as _pydantic


class _BaseProgram(_pydantic.BaseModel):
    name: str
    description: str
    level: str
    term: str
    journies: str
    status: str


class Program(_BaseProgram):
    id: int
    formation_area_id: int
    created_at: _dt.datetime
    updated_at: _dt.datetime

    class Config:
        orm_mode = True
        from_attributes = True


class CreateProgram(_BaseProgram):
    pass
