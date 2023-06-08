from fastapi import APIRouter
from fastapi.responses import JSONResponse
# from fastapi.encoders import jsonable_encoder
from controllers.users import add_user
from pydantic import BaseModel, constr, EmailStr, Field

router = APIRouter()

class CreateUser(BaseModel):
  name: str = Field(min_length=2, max_length=30)
  surname: str = Field(min_length=2, max_length=30)
  age: int = Field(gt=13, lt=100)
  email: EmailStr
  password: constr(min_length=5)
    
@router.post('/')
def get_create_user(user: CreateUser):
  res = add_user(user)

  return JSONResponse({ 'user': res})