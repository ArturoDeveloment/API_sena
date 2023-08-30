from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

app = FastAPI(debug=True)
templates = Jinja2Templates("./templates")

@app.get("/")
def index():
    return {"message": "Hello world"}

def get_app():
    return app