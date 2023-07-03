from pydantic import BaseModel, EmailStr, Field, HttpUrl
from typing import Optional

class CreateUser(BaseModel):
  name: str = Field(min_length=2, max_length=30)
  surname: str = Field(min_length=2, max_length=30)
  email: EmailStr
  password: str = Field(min_length=5)

class AuthUser(BaseModel):
  email: EmailStr
  password: str

class UpdateUser(BaseModel):
  name: Optional[str] = Field(min_length=2, max_length=30)
  surname: Optional[str] = Field(min_length=2, max_length=30)
  email: Optional[EmailStr]
  password: Optional[str] = Field(min_length=5)

class CreateItem(BaseModel):
  img_url: HttpUrl
  name: str = Field(min_length=2, max_length=40)
  desc: str = Field(min_length=20, max_length=1000)
  tags: list

class EditItem(BaseModel):
  img_url: HttpUrl
  name: str = Field(min_length=2, max_length=40)
  desc: str = Field(min_length=20, max_length=1000)
  tags: list