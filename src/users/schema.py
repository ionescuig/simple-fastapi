from uuid import UUID

from pydantic import BaseModel, EmailStr


class UserCreateSchema(BaseModel):
    username: str
    email: EmailStr
    first_name: str
    last_name: str
    password: str

    class Config:
        orm_mode = True


class UserSchema(BaseModel):
    id: UUID | None = None
    username: str
    email: EmailStr
    first_name: str
    last_name: str

    class Config:
        orm_mode = True
