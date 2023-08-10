from fastapi import APIRouter, Request
from models.user_data import Admin
from fastapi import HTTPException
from app import templates

admin = APIRouter()

class Auth:
    __data = {}
    def set_data(self, **kwargs):
        self.__data = kwargs.get("data")
    
    def logout_data(self):
        self.__data.clear()

auth_session = Auth()

def session(func):
    def wrapper(*args, **kwargs):
        if "data" in kwargs:
            auth_session.set_data(data = kwargs.get("data"))
            return func(*args, **kwargs)
        else:
            raise HTTPException(status_code=404, detail="Formation area does not exist")
    return wrapper


@admin.get("/admin")
def get_template(request: Request):
    context = {
        "request": request,
        "username": "admin"
    }
    return templates.TemplateResponse( name="admin.html", context=context)

@session
@admin.post("/admin")
def auth_user(data: Admin):
    pass

@session
@admin.get("/logout")
def logout():
    pass