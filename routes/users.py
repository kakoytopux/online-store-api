from fastapi import APIRouter, Request
from controllers.users import get_user_info, get_user_changed
from middlewares.validator import UpdateUser

router = APIRouter()

@router.get('/me')
def get_user_me(req: Request):
  return get_user_info(req)

@router.patch('/me')
def get_user_me(req: Request, user: UpdateUser):
  return get_user_changed(req, user)