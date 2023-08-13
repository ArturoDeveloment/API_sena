from fastapi import APIRouter
from typing import TYPE_CHECKING, List
import fastapi as _fastapi
import sqlalchemy.orm as orm

from schemas import offices_schemas
from services import office_services, database_services

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/office", response_model=offices_schemas.Offices)
async def create_office(
        office: offices_schemas.CreateOffices,
        db: orm.Session = _fastapi.Depends(database_services.get_db)
):
    return await office_services.create_office(office=office, db=db)


@router.get("/offices", response_model=List[offices_schemas.Offices])
async def get_offices(
        db: orm.Session = _fastapi.Depends(database_services.get_db)
):
    return await office_services.get_all_offices(db=db)


@router.get("/office/{office_id}", response_model=offices_schemas.Offices)
async def get_office(
        office_id: int,
        db: orm.Session = _fastapi.Depends(database_services.get_db)
):
    office = await office_services.get_office(office_id=office_id, db=db)
    if office_id is None:
        raise _fastapi.HTTPException(status_code=404, detail="Office does not exist")

    return office


@router.delete("/office/{office_id}")
async def delete_office(
        office_id: int, db: orm.Session = _fastapi.Depends(database_services.get_db)
):
    office = await office_services.get_office(office_id=office_id, db=db)
    if office_id is None:
        raise _fastapi.HTTPException(status_code=404, detail="Office does not exist")

    await office_services.delete_office(office, db=db)
    return "Successfully deleted the office"


@router.put("/office/{office_id}", response_model=offices_schemas.Offices)
async def update_office(
    office_id: int,
    office_data: offices_schemas.CreateOffices,
    db: orm.Session = _fastapi.Depends(database_services.get_db)
):
    office = await office_services.get_office(office_id=office_id, db=db)
    if office is None:
        raise _fastapi.HTTPException(status_code=404, detail="Office does not exist")

    return await office_services.update_office(
        office_data=office_data,
        office=office,
        db=db
    )
