from fastapi import FastAPI
from routes.users import router as user_router
from controllers.users import create_user
from controllers.signin import auth_user
from middlewares.validator import CreateUser, AuthUser

app = FastAPI()

@app.post('/signup')
def get_create_user(user: CreateUser):
  res = create_user(user)

  return res

@app.post('/signin')
def get_auth_user(user: AuthUser):
  res = auth_user(user)

  return res

app.include_router(user_router)
