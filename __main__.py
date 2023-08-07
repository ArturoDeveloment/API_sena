from uvicorn import run
from app import get_app
from routes.formation_area_routes import router as formation_areas_router
from routes.program_routes import router as program_router

app = get_app()


app.include_router(formation_areas_router)
app.include_router(program_router)


if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8000)
