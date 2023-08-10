from pydantic import BaseModel

class Admin(BaseModel):
    user_name: str
    passwd: str
    token: str