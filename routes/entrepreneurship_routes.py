from fastapi import APIRouter
from typing import TYPE_CHECKING, List
import fastapi as _fastapi
import sqlalchemy.orm as orm

from schemas import entrepreneurship_schema
from services import entrepreneurship_services, database_services

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/entrepreneurship", response_model=entrepreneurship_schema.Entrepreneurship)
async def create_entrepreneurship(
        entrepreneurship: entrepreneurship_schema.CreateEntrepreneurship,
        db: orm.Session = _fastapi.Depends(database_services.get_db)
):
    return await entrepreneurship_services.create_entrepreneurship(entrepreneurship=entrepreneurship, db=db)


@router.get("/entrepreneurships", response_model=List[entrepreneurship_schema.Entrepreneurship])
async def get_entrepreneurships(
        db: orm.Session = _fastapi.Depends(database_services.get_db)
):
    return await entrepreneurship_services.get_all_entrepreneurships(db=db)


@router.get("/entrepreneurship/{entrepreneurship_id}", response_model=entrepreneurship_schema.Entrepreneurship)
async def get_entrepreneurship(
        entrepreneurship_id: int,
        db: orm.Session = _fastapi.Depends(database_services.get_db)
):
    entrepreneurship = await entrepreneurship_services.get_entrepreneurship(entrepreneurship_id=entrepreneurship_id, db=db)
    if entrepreneurship is None:
        raise _fastapi.HTTPException(status_code=404, detail="entrepreneurship  does not exist")

    return entrepreneurship


@router.delete("/entrepreneurships/{entrepreneurship_id}")
async def delete_entrepreneurship(
        entrepreneurship_id: int, db: orm.Session = _fastapi.Depends(database_services.get_db)
):
    entrepreneurship = await entrepreneurship_services.get_entrepreneurship(entrepreneurship_id=entrepreneurship_id, db=db)
    if entrepreneurship is None:
        raise _fastapi.HTTPException(status_code=404, detail="entrepreneurship  does not exist")

    await entrepreneurship_services.delete_entrepreneurship(entrepreneurship, db=db)
    return "Successfully deleted the entrepreneurship "


@router.put("/entrepreneurships/{entrepreneurship_id}", response_model=entrepreneurship_schema.Entrepreneurship)
async def update_entrepreneurship(
    entrepreneurship_id: int,
    entrepreneurship_data: entrepreneurship_schema.CreateEntrepreneurship,
    db: orm.Session = _fastapi.Depends(database_services.get_db)
):
    entrepreneurship = await entrepreneurship_services.get_entrepreneurship(entrepreneurship_id=entrepreneurship_id, db=db)
    if entrepreneurship is None:
        raise _fastapi.HTTPException(status_code=404, detail="entrepreneurship  does not exist")

    return await entrepreneurship_services.update_entrepreneurship(
        entrepreneurship_data=entrepreneurship_data,
        entrepreneurship=entrepreneurship,
        db=db
    )
