import datetime as _dt
import pydantic as _pydantic


class _BaseOffices(_pydantic.BaseModel):
    name: str
    description: str
    partners : str
    status: str

    

class Office(_BaseOffices):
    id: int
    created_at: _dt.datetime
    updated_at: _dt.datetime

    class Config:
        orm_mode = True
        from_attributes = True


class CreateOffice(_BaseOffices):
    pass
