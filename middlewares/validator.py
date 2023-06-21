from pydantic import BaseModel, EmailStr, Field
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