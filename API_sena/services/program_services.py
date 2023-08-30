from typing import TYPE_CHECKING

from db import database
from models import program_model
from schemas import program_schema
from services import formation_area_services
import fastapi as _fastapi


if TYPE_CHECKING:
    from sqlalchemy.orm import Session


async def create_program(
        formation_area_id: int,
        program: program_schema.CreateProgram,
        db: "Session"
) -> program_schema.Program:
    formation_area = await formation_area_services.get_formation_area(formation_area_id=formation_area_id, db=db)
    if formation_area is None:
        raise _fastapi.HTTPException(status_code=404, detail="Formation area does not exist")

    program_data = program.dict()
    program_data["formation_area_id"] = formation_area_id

    program_model_instance = program_model.Program(**program_data)
    db.add(program_model_instance)
    db.commit()
    db.refresh(program_model_instance)
    return program_schema.Program.from_orm(program_model_instance)


async def get_all_programs(
        formation_area_id: int,
        db: "Session"
) -> list[program_schema.Program]:
    formation_area = await formation_area_services.get_formation_area(formation_area_id=formation_area_id, db=db)
    if formation_area is None:
        raise _fastapi.HTTPException(status_code=404, detail="Formation area does not exist")

    programs = db.query(program_model.Program).filter(program_model.Program.formation_area_id == formation_area_id).all()
    return list(map(program_schema.Program.from_orm, programs))


async def get_program(
        formation_area_id: int,
        program_id: int,
        db: "Session"
):
    formation_area = await formation_area_services.get_formation_area(formation_area_id=formation_area_id, db=db)
    if formation_area is None:
        raise _fastapi.HTTPException(status_code=404, detail="Formation area does not exist")

    program = db.query(program_model.Program).filter(program_model.Program.formation_area_id == formation_area_id).filter(program_model.Program.id == program_id).first()
    return program


async def delete_program(
        program: int,
        db: "Session"
):
    db.delete(program)
    db.commit()


async def update_program(
        program_data: program_schema.CreateProgram,
        program: program_model.Program,
        db: "Session"
) -> program_schema.Program:
    program.name = program_data.name
    program.description = program_data.description
    program.level = program_data.level
    program.term = program_data.term
    program.journies = program_data.journies
    program.status = program_data.status

    db.commit()
    db.refresh(program)

    return program_schema.Program.from_orm(program)
