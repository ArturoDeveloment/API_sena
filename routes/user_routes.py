from fastapi import APIRouter
from typing import TYPE_CHECKING, List
import fastapi as _fastapi
import sqlalchemy.orm as orm

from schemas import user_schema
from services import user_services, database_services

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/user", response_model=user_schema.User)
async def create_user(
        user: user_schema.CreateUser,
        db: orm.Session = _fastapi.Depends(database_services.get_db)
):
    return await user_services.create_user(user=user, db=db)


@router.get("/users", response_model=List[user_schema.User])
async def get_users(
        db: orm.Session = _fastapi.Depends(database_services.get_db)
):
    return await user_services.get_all_users(db=db)


@router.get("/user/{user_id}", response_model=user_schema.User)
async def get_user(
        user_id: int,
        db: orm.Session = _fastapi.Depends(database_services.get_db)
):
    user = await user_services.get_user(user_id=user_id, db=db)
    if user is None:
        raise _fastapi.HTTPException(status_code=404, detail="User does not exist")

    return user


@router.delete("/users/{user_id}")
async def delete_user(
        user_id: int, db: orm.Session = _fastapi.Depends(database_services.get_db)
):
    user = await user_services.get_user(user_id=user_id, db=db)
    if user is None:
        raise _fastapi.HTTPException(status_code=404, detail="User does not exist")

    await user_services.delete_user(user, db=db)
    return "Successfully deleted the User"


@router.put("/users/{user_id}", response_model=user_schema.User)
async def update_user(
    user_id: int,
    user_data: user_schema.CreateUser,
    db: orm.Session = _fastapi.Depends(database_services.get_db)
):
    user = await user_services.get_user(user_id=user_id, db=db)
    if user is None:
        raise _fastapi.HTTPException(status_code=404, detail="User does not exist")

    return await user_services.update_user(
        user_data=user_data,
        user=user,
        db=db
    )
