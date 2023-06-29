from fastapi import FastAPI, Depends
from routes.users import router as user_router
from routes.items_admin import router as item_router
from controllers.users import create_user
from controllers.signin import auth_user
from middlewares.validator import CreateUser, AuthUser
from middlewares.auth import auth
from middlewares.auth_admin import auth_admin
from dotenv import load_dotenv
import uvicorn

load_dotenv()

app = FastAPI()

@app.post('/signup')
def get_create_user(user: CreateUser):
  return create_user(user)

@app.post('/signin')
def get_auth_user(user: AuthUser):
  return auth_user(user)

app.include_router(user_router, prefix='/users', dependencies=[Depends(auth)])
app.include_router(item_router, prefix='/items', dependencies=[Depends(auth), Depends(auth_admin)])


if __name__ == '__main__':
  uvicorn.run('app:app', host='localhost', port=5001, reload=True)