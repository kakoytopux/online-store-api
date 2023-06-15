from fastapi import FastAPI, Depends
from routes.users import router as user_router
from controllers.users import create_user
from controllers.signin import auth_user
from middlewares.validator import CreateUser, AuthUser
from middlewares.auth import auth

app = FastAPI()

@app.post('/signup')
def get_create_user(user: CreateUser):
  return create_user(user)

@app.post('/signin')
def get_auth_user(user: AuthUser):
  return auth_user(user)

app.include_router(user_router, dependencies=[Depends(auth)])
