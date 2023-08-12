from fastapi import APIRouter, Request
from models.user_data import Admin
from app import templates

admin = APIRouter()

class Auth:
    __data = {}
    def set_data(self, **kwargs):
        if "data" in self.__data.keys():
            print("You are alredy logged")
            return False
        
        if self.__verify_credentials(kwargs.get("data")):
            print("User logged successfully!")
            self.__data["data"] = kwargs.get("data")
            return True

        return False
    
    def delete_credentials(self):
        self.__data.clear()
    
    def __verify_credentials(self, data: dict):
        import os 
        user = os.getenv("USER_ADMIN") or ""
        password = os.getenv("PASSWORD_ADMIN") or ""
        
        data = data.copy()
        
        if user.__eq__(data.get("user_name")) and password.__eq__(data.get("password")):
            return True
        return False
    
    def get_data(self):
        return self.__data

auth_session = Auth()

def session(func):
    def wrapper(*args, **kwargs):
        if "data" in kwargs:
            return auth_session.set_data(data = kwargs.get("data"))
        else:
            return False
    return wrapper

def logout(func):
    def wrapper(*args, **kwargs):
        auth_session.delete_credentials()
    return wrapper

@admin.get("/admin")
def get_template(request: Request):
    context = {
        "request": request,
        "username": "admin"        
    }
    return templates.TemplateResponse( name="admin.html", context=context)

@admin.post("/admin")
def auth_user(data: Admin):
    @session
    def auth(data):
        pass
    result = auth(data=data.dict())
    print(result)
    return auth_session.get_data()


@admin.get("/logout")
def exit_admin():
    @logout
    def exit():
        pass
    exit()
    return auth_session.get_data()