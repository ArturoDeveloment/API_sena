from fastapi import APIRouter
from typing import TYPE_CHECKING, List
import fastapi as _fastapi
import sqlalchemy.orm as orm

from schemas import formation_area_schema
from services import formation_area_services, database_services

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/formation_area", response_model=formation_area_schema.FormationArea)
async def create_formation_area(
        formation_area: formation_area_schema.CreateFormationArea,
        db: orm.Session = _fastapi.Depends(database_services.get_db)
):
    return await formation_area_services.create_formation_area(formation_area=formation_area, db=db)


@router.get("/formation_areas", response_model=List[formation_area_schema.FormationArea])
async def get_formation_areas(
        db: orm.Session = _fastapi.Depends(database_services.get_db)
):
    return await formation_area_services.get_all_formation_areas(db=db)


@router.get("/formation_area/{formation_area_id}", response_model=formation_area_schema.FormationArea)
async def get_formation_area(
        formation_area_id: int,
        db: orm.Session = _fastapi.Depends(database_services.get_db)
):
    formation_area = await formation_area_services.get_formation_area(formation_area_id=formation_area_id, db=db)
    if formation_area is None:
        raise _fastapi.HTTPException(status_code=404, detail="Formation area does not exist")

    return formation_area


@router.delete("/formation_areas/{formation_area_id}")
async def delete_formation_area(
        formation_area_id: int, db: orm.Session = _fastapi.Depends(database_services.get_db)
):
    formation_area = await formation_area_services.get_formation_area(formation_area_id=formation_area_id, db=db)
    if formation_area is None:
        raise _fastapi.HTTPException(status_code=404, detail="Formation area does not exist")

    await formation_area_services.delete_formation_area(formation_area, db=db)
    return "Successfully deleted the formation area"


@router.put("/formation_areas/{formation_area_id}", response_model=formation_area_schema.FormationArea)
async def update_formation_area(
    formation_area_id: int,
    formation_area_data: formation_area_schema.CreateFormationArea,
    db: orm.Session = _fastapi.Depends(database_services.get_db)
):
    formation_area = await formation_area_services.get_formation_area(formation_area_id=formation_area_id, db=db)
    if formation_area is None:
        raise _fastapi.HTTPException(status_code=404, detail="Formation area does not exist")

    return await formation_area_services.update_formation_area(
        formation_area_data=formation_area_data,
        formation_area=formation_area,
        db=db
    )
