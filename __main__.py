from uvicorn import run
from app import get_app
from routes.formation_area_routes import router as formation_areas_router
from routes.program_routes import router as program_router
from routes.auth_admin import admin
from routes.offices_routes import router as office_router
from routes.entrepreneurship_routes import router as entrepreneurship_router
from routes.well_being_route import router as well_being_router
from routes.user_routes import router as user_router
from services.database_services import create_tables

app = get_app()


app.include_router(formation_areas_router)
app.include_router(program_router)
app.include_router(office_router)
app.include_router(entrepreneurship_router)
app.include_router(well_being_router)
app.include_router(user_router)
app.include_router(admin)


if __name__ == "__main__":
    create_tables()
    run(app, host="127.0.0.1", port=8000)

