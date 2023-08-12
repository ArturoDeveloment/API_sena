import datetime as _dt
import pydantic as _pydantic


class _BaseFormationArea(_pydantic.BaseModel):
    name: str
    description: str
    status: str
    

class FormationArea(_BaseFormationArea):
    id: int
    created_at: _dt.datetime
    updated_at: _dt.datetime

    class Config:
        orm_mode = True
        from_attributes = True


class CreateFormationArea(_BaseFormationArea):
    pass
