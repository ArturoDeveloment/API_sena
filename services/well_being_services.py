from typing import TYPE_CHECKING

from db import database
from models import well_being_model
from schemas import well_being_schema


if TYPE_CHECKING:
    from sqlalchemy.orm import Session


async def create_well_being(
        well_being: well_being_schema.CreateWellBeing,
        db: "Session"
) -> well_being_schema.WellBeing:
    well_being = well_being_model.WellBeing(**well_being.dict())
    db.add(well_being)
    db.commit()
    db.refresh(well_being)
    return well_being_schema.WellBeing.from_orm(well_being)


async def get_all_well_beings(
        db: "Session"
) -> list[well_being_schema.WellBeing]:
    well_beings = db.query(well_being_model.WellBeing).all()
    return list(map(well_being_schema.WellBeing.from_orm, well_beings))


async def get_well_being(
        well_being_id: int,
        db: "Session"
):
    well_being = db.query(well_being_model.WellBeing).filter(well_being_model.WellBeing.id == well_being_id).first()
    return well_being


async def delete_well_being(
        well_being: well_being_model.WellBeing,
        db: "Session"
):
    db.delete(well_being)
    db.commit()


async def update_well_being(
        well_being_data: well_being_schema.CreateWellBeing,
        well_being: well_being_model.WellBeing,
        db: "Session"
) -> well_being_schema.WellBeing:
    well_being.name = well_being_data.name
    well_being.description = well_being_data.description
    well_being.status = well_being_data.status

    db.commit()
    db.refresh(well_being)

    return well_being_schema.WellBeing.from_orm(well_being)
