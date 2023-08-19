from fastapi import APIRouter
from typing import TYPE_CHECKING, List
import fastapi as _fastapi
import sqlalchemy.orm as orm

from schemas import well_being_schema
from services import well_being_services, database_services

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/well_being", response_model=well_being_schema.WellBeing)
async def create_well_being(
        well_being: well_being_schema.CreateWellBeing,
        db: orm.Session = _fastapi.Depends(database_services.get_db)
):
    return await well_being_services.create_well_being(well_being=well_being, db=db)


@router.get("/well_beings", response_model=List[well_being_schema.WellBeing])
async def get_well_beings(
        db: orm.Session = _fastapi.Depends(database_services.get_db)
):
    return await well_being_services.get_all_well_beings(db=db)


@router.get("/well_being/{well_being_id}", response_model=well_being_schema.WellBeing)
async def get_well_being(
        well_being_id: int,
        db: orm.Session = _fastapi.Depends(database_services.get_db)
):
    well_being = await well_being_services.get_well_being(well_being_id=well_being_id, db=db)
    if well_being is None:
        raise _fastapi.HTTPException(status_code=404, detail="well being area does not exist")

    return well_being


@router.delete("/well_beings/{well_being_id}")
async def delete_well_being(
        well_being_id: int, db: orm.Session = _fastapi.Depends(database_services.get_db)
):
    well_being = await well_being_services.get_well_being(well_being_id=well_being_id, db=db)
    if well_being is None:
        raise _fastapi.HTTPException(status_code=404, detail="well being area does not exist")

    await well_being_services.delete_well_being(well_being, db=db)
    return "Successfully deleted the well being area"


@router.put("/well_beings/{well_being_id}", response_model=well_being_schema.WellBeing)
async def update_well_being(
    well_being_id: int,
    well_being_data: well_being_schema.CreateWellBeing,
    db: orm.Session = _fastapi.Depends(database_services.get_db)
):
    well_being = await well_being_services.get_well_being(well_being_id=well_being_id, db=db)
    if well_being is None:
        raise _fastapi.HTTPException(status_code=404, detail="well being area does not exist")

    return await well_being_services.update_well_being(
        well_being_data=well_being_data,
        well_being=well_being,
        db=db
    )
