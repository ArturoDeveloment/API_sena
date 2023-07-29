from fastapi import FastAPI

app = FastAPI(debug=True)

@app.get("/")
def index():
    return {"message": "Hello world"}

def get_app():
    return app