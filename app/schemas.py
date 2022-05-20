from pydantic import BaseModel


class Token(BaseModel):
    token: str


class UserBase(BaseModel):
    email: str


class UserAuthentication(UserBase):
    password: str


class ResponseSchema(BaseModel):
    message: str
