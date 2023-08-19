from typing import TYPE_CHECKING

from db import database
from models import office_model
from schemas import offices_schemas


if TYPE_CHECKING:
    from sqlalchemy.orm import Session


async def create_office(
        office: offices_schemas.CreateOffices,
        db: "Session"
) -> offices_schemas.Offices:
    office = office_model.Office(**office.dict())
    db.add(office)
    db.commit()
    db.refresh(office)
    return offices_schemas.Offices.from_orm(office)


async def get_all_offices(
        db: "Session"
) -> list[offices_schemas.Offices]:
    offices = db.query(office_model.Office).all()
    return list(map(offices_schemas.Offices.from_orm, offices))


async def get_office(
        office_id: int,
        db: "Session"
):
    office = db.query(office_model.Office).filter(office_model.Office.id == office_id).first()
    return office


async def delete_office(
        office: office_model.Office,
        db: "Session"
):
    db.delete(office)
    db.commit()


async def update_office(
        office_data: offices_schemas.CreateOffices,
        office: office_model.Office,
        db: "Session"
) -> offices_schemas.Offices:
    office.name = office_data.name
    office.description = office_data.description
    office.status = office_data.status

    db.commit()
    db.refresh(office)

    return offices_schemas.Offices.from_orm(office)
