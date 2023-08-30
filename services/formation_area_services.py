from typing import TYPE_CHECKING

from db import database
from models import formation_area_model
from schemas import formation_area_schema


if TYPE_CHECKING:
    from sqlalchemy.orm import Session


async def create_formation_area(
        formation_area: formation_area_schema.CreateFormationArea,
        db: "Session"
) -> formation_area_schema.FormationArea:
    formation_area = formation_area_model.FormationArea(**formation_area.dict())
    db.add(formation_area)
    db.commit()
    db.refresh(formation_area)
    return formation_area_schema.FormationArea.from_orm(formation_area)


async def get_all_formation_areas(
        db: "Session"
) -> list[formation_area_schema.FormationArea]:
    formation_areas = db.query(formation_area_model.FormationArea).all()
    return list(map(formation_area_schema.FormationArea.from_orm, formation_areas))


async def get_formation_area(
        formation_area_id: int,
        db: "Session"
):
    formation_area = db.query(formation_area_model.FormationArea).filter(formation_area_model.FormationArea.id == formation_area_id).first()
    return formation_area


async def delete_formation_area(
        formation_area: formation_area_model.FormationArea,
        db: "Session"
):
    db.delete(formation_area)
    db.commit()


async def update_formation_area(
        formation_area_data: formation_area_schema.CreateFormationArea,
        formation_area: formation_area_model.FormationArea,
        db: "Session"
) -> formation_area_schema.FormationArea:
    formation_area.name = formation_area_data.name
    formation_area.description = formation_area_data.description
    formation_area.status = formation_area_data.status

    db.commit()
    db.refresh(formation_area)

    return formation_area_schema.FormationArea.from_orm(formation_area)
