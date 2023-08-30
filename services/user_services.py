from typing import TYPE_CHECKING

from db import database
from models import user_model
from schemas import user_schema


if TYPE_CHECKING:
    from sqlalchemy.orm import Session


async def create_user(
        user: user_schema.CreateUser,
        db: "Session"
) -> user_schema.User:
    user = user_model.UserModel(**user.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user_schema.User.from_orm(user)


async def get_all_users(
        db: "Session"
) -> list[user_schema.User]:
    users = db.query(user_model.UserModel).all()
    return list(map(user_schema.User.from_orm, users))


async def get_user(
        user_id: int,
        db: "Session"
):
    user = db.query(user_model.UserModel).filter(user_model.UserModel.id == user_id).first()
    return user


async def delete_user(
        user: user_model.UserModel,
        db: "Session"
):
    db.delete(user)
    db.commit()


async def update_user(
        user_data: user_schema.CreateUser,
        user: user_model.UserModel,
        db: "Session"
) -> user_schema.User:
    user.user_name = user_data.user_name
    user.password = user_data.password
    user.token = user_data.token

    db.commit()
    db.refresh(user)

    return user_schema.User.from_orm(user)
