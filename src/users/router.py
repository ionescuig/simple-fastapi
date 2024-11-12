# ruff: noqa: B008 - function-call-in-default-argument
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from settings.database import get_session
from users.models import User
from users.schema import UserCreateSchema, UserSchema

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=list[UserSchema])
async def get_all_users(session: AsyncSession = Depends(get_session)):
    """Get all users."""
    result = await session.execute(select(User))
    return result.scalars().all()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserSchema)
async def create_user(
    user: UserCreateSchema,
    session: AsyncSession = Depends(get_session),
):
    """Create a new user."""
    try:
        new_user = User(**user.model_dump())
        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)
        return new_user
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)) from e


# @router.get("/{uuid}")
# async def get_user(uuid: UUID):
#     """Get all users."""
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
#     # return [{"username": "Rick"}, {"username": "Morty"}]
