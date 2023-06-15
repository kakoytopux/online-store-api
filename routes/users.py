from fastapi import APIRouter, Request
from controllers.users import get_info_user

router = APIRouter()

@router.get('/users/me')
def get_user_me(req: Request):
  return get_info_user(req)