from fastapi import FastAPI
from routes.users import router as user_router
from controllers.users import create_user
from middlewares.validator import CreateUser
from mysql.connector import connect, Error

app = FastAPI()

try:
  conn = connect(
    host='localhost',
    user='root',
    password='',
    database='online_store'
  )

  cur = conn.cursor()

  cur.execute("CREATE DATABASE IF NOT EXISTS online_store")

  conn.commit()
  cur.close()
  conn.close()
except Error as err:
  print(err)


@app.post('/signup')
def get_create_user(user: CreateUser):
  res = create_user(user)

  return res

app.include_router(user_router)
