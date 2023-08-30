import datetime as _dt
import pydantic as _pydantic


class _BaseUser(_pydantic.BaseModel):
    user_name: str
    password: str
    token: str
    

class User(_BaseUser):
    id: int
    created_at: _dt.datetime
    updated_at: _dt.datetime

    class Config:
        orm_mode = True
        from_attributes = True


class CreateUser(_BaseUser):
    pass
