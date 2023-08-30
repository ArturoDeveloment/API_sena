import datetime as _dt
import pydantic as _pydantic


class _BaseWellBeing(_pydantic.BaseModel):
    name: str
    description: str
    partners: str
    aditional_info: str
    status: str

class WellBeing(_BaseWellBeing):
    id: int
    created_at: _dt.datetime
    updated_at: _dt.datetime

    class Config:
        orm_mode = True
        from_attributes = True


class CreateWellBeing(_BaseWellBeing):
    pass
