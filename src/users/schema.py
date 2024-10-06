from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    full_name: str
    password: str

    class Config:
        orm_mode = True
