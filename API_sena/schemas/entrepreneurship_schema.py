import datetime as _dt
import pydantic as _pydantic


class _BaseEntrepreneurship(_pydantic.BaseModel):
    name: str
    description: str
    applications: str
    partners: str
    comments: str
    status: str
    

class Entrepreneurship(_BaseEntrepreneurship):
    id: int
    created_at: _dt.datetime
    updated_at: _dt.datetime

    class Config:
        orm_mode = True
        from_attributes = True


class CreateEntrepreneurship(_BaseEntrepreneurship):
    pass
