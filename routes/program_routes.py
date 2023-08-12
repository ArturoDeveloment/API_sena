from fastapi import APIRouter
from typing import TYPE_CHECKING, List
import fastapi as _fastapi
import sqlalchemy.orm as orm

from schemas import program_schema
from services import formation_area_services, program_services, database_services


if TYPE_CHECKING:
    from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/{formation_area_id}/program", response_model=program_schema.Program)
async def create_program(
        formation_area_id: int,
        program: program_schema.CreateProgram,
        db: orm.Session = _fastapi.Depends(database_services.get_db)
):
    formation_area = await formation_area_services.get_formation_area(formation_area_id=formation_area_id, db=db)
    if formation_area is None:
        raise _fastapi.HTTPException(status_code=404, detail="Formation area does not exist")
    return await program_services.create_program(formation_area_id=formation_area_id,
                                                 program=program, db=db)


@router.get("/{formation_area_id}/programs", response_model=List[program_schema.Program])
async def get_programs(
        formation_area_id: int,
        db: orm.Session = _fastapi.Depends(database_services.get_db)
):
    formation_area = await formation_area_services.get_formation_area(formation_area_id=formation_area_id, db=db)
    if formation_area is None:
        raise _fastapi.HTTPException(status_code=404, detail="Formation area does not exist")
    return await program_services.get_all_programs(formation_area_id=formation_area_id, db=db)


@router.get("/{formation_area_id}/program/{program_id}", response_model=program_schema.Program)
async def get_program(
        formation_area_id: int,
        program_id: int,
        db: orm.Session = _fastapi.Depends(database_services.get_db)
):
    formation_area = await formation_area_services.get_formation_area(formation_area_id=formation_area_id, db=db)
    if formation_area is None:
        raise _fastapi.HTTPException(status_code=404, detail="Formation area does not exist")

    program = await program_services.get_program(formation_area_id=formation_area_id,
                                                 program_id=program_id, db=db)
    if program is None:
        raise _fastapi.HTTPException(status_code=404, detail="Program does not exist")

    return program


@router.delete("/{formation_area_id}/program/{program_id}")
async def delete_program(
        formation_area_id: int,
        program_id: int,
        db: orm.Session = _fastapi.Depends(database_services.get_db)
):
    formation_area = await formation_area_services.get_formation_area(formation_area_id=formation_area_id, db=db)
    if formation_area is None:
        raise _fastapi.HTTPException(status_code=404, detail="Formation area does not exist")

    program = await program_services.get_program(formation_area_id=formation_area_id,
                                                 program_id=program_id, db=db)
    if program is None:
        raise _fastapi.HTTPException(status_code=404, detail="Program does not exist")

    await program_services.delete_program(program=program, db=db)
    return "Successfully deleted the program"


@router.put("/{formation_area_id}/program/{program_id}", response_model=program_schema.Program)
async def update_program(
    formation_area_id: int,
    program_id: int,
    program_data: program_schema.CreateProgram,
    db: orm.Session = _fastapi.Depends(database_services.get_db)
):
    formation_area = await formation_area_services.get_formation_area(formation_area_id=formation_area_id, db=db)
    if formation_area is None:
        raise _fastapi.HTTPException(status_code=404, detail="Formation area does not exist")

    program = await program_services.get_program(formation_area_id=formation_area_id,
                                                 program_id=program_id, db=db)
    if program is None:
        raise _fastapi.HTTPException(status_code=404, detail="Program does not exist")

    return await program_services.update_program(
        program_data=program_data,
        program=program,
        db=db
    )
