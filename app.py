from fastapi import FastAPI
from fastapi.responses import JSONResponse
from routes.users import router as user_router
from controllers.users import create_user
from middlewares.validator import CreateUser

app = FastAPI()

@app.post('/signup')
def get_create_user(user: CreateUser):
  res = create_user(user)

  return JSONResponse({ 'user': res }, status_code=201)

app.include_router(user_router)
