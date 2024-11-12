from uuid import UUID

from pydantic import BaseModel, EmailStr


class UserCreateSchema(BaseModel):
    username: str
    email: EmailStr
    full_name: str
    password: str

    class Config:
        orm_mode = True


class UserSchema(UserCreateSchema):
    id: UUID | None = None

    class Config:
        orm_mode = True
