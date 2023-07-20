from fastapi import APIRouter, Depends, Request
from routes.users import router as user_router
from routes.items_admin import router as item_router_admin
from routes.items import router as item_router
from controllers.users import create_user
from controllers.signin import auth_user
from controllers.signout import exit_user
from controllers.items import get_items_all
from middlewares.validator import CreateUser, AuthUser
from middlewares.auth import auth
from middlewares.auth_admin import auth_admin

router = APIRouter()

@router.post('/signup')
def get_create_user(user: CreateUser):
  return create_user(user)

@router.post('/signin')
def get_auth_user(user: AuthUser):
  return auth_user(user)

@router.delete('/signout')
def get_exit_user(req: Request):
  return exit_user(req)

@router.get('/items')
def get_items():
  return get_items_all()

router.include_router(user_router, prefix='/users', dependencies=[Depends(auth)])
router.include_router(item_router, prefix='/items', dependencies=[Depends(auth)])
router.include_router(item_router_admin, prefix='/items/admin',
                   dependencies=[Depends(auth), Depends(auth_admin)])
