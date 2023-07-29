from uvicorn import run
from app import get_app

app = get_app()

if __name__ == "__main__":
    run(app, host = "0.0.0.0", port = 8000)

