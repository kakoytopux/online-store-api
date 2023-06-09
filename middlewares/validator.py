from pydantic import BaseModel, constr, EmailStr, Field

class CreateUser(BaseModel):
  name: str = Field(min_length=2, max_length=30)
  surname: str = Field(min_length=2, max_length=30)
  age: int = Field(gt=13, lt=100)
  email: EmailStr
  password: constr(min_length=5)