from typing import TYPE_CHECKING

from db import database
from models import entrepreneurship_model
from schemas import entrepreneurship_schema


if TYPE_CHECKING:
    from sqlalchemy.orm import Session


async def create_entrepreneurship(
        entrepreneurship: entrepreneurship_schema.CreateEntrepreneurship,
        db: "Session"
) -> entrepreneurship_schema.Entrepreneurship:
    entrepreneurship = entrepreneurship_model.Entrepreneurship(**entrepreneurship.dict())
    db.add(entrepreneurship)
    db.commit()
    db.refresh(entrepreneurship)
    return entrepreneurship_schema.Entrepreneurship.from_orm(entrepreneurship)


async def get_all_entrepreneurships(
        db: "Session"
) -> list[entrepreneurship_schema.Entrepreneurship]:
    entrepreneurships = db.query(entrepreneurship_model.Entrepreneurship).all()
    return list(map(entrepreneurship_schema.Entrepreneurship.from_orm, entrepreneurships))


async def get_entrepreneurship(
        entrepreneurship_id: int,
        db: "Session"
):
    entrepreneurship = db.query(entrepreneurship_model.Entrepreneurship).filter(entrepreneurship_model.Entrepreneurship.id == entrepreneurship_id).first()
    return entrepreneurship


async def delete_entrepreneurship(
        entrepreneurship: entrepreneurship_model.Entrepreneurship,
        db: "Session"
):
    db.delete(entrepreneurship)
    db.commit()


async def update_entrepreneurship(
        entrepreneurship_data: entrepreneurship_schema.CreateEntrepreneurship,
        entrepreneurship: entrepreneurship_model.Entrepreneurship,
        db: "Session"
) -> entrepreneurship_schema.Entrepreneurship:
    entrepreneurship.name = entrepreneurship_data.name
    entrepreneurship.description = entrepreneurship_data.description
    entrepreneurship.status = entrepreneurship_data.status

    db.commit()
    db.refresh(entrepreneurship)

    return entrepreneurship_schema.Entrepreneurship.from_orm(entrepreneurship)
