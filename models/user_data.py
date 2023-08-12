from pydantic import BaseModel

class Admin(BaseModel):
    user_name: str
    password: str
    token: str