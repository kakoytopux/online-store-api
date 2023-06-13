from sqlalchemy import select
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from operator import attrgetter
from models.user import User
from middlewares.db import db
import bcrypt
import jwt

def auth_user(user):
  session = db.get_session()
  email, password = attrgetter('email', 'password')(user)

  email_db = select(User).where(User.email == email)
  user_obj = None

  for res in session.execute(email_db).scalars():
    user_obj = res

  if user_obj:
    password_valid = bcrypt.checkpw(password.encode('utf-8'), user_obj.password.encode('utf-8'))

    if password_valid:
      token = jwt.encode({ 'email': user_obj.email }, 'secret-dev', algorithm='HS256')
      
      res = JSONResponse(content='')
      res.set_cookie(key='token', value=token)

      return res
    else:
      raise HTTPException(detail={ 'message': 'Введены неверные данные.' }, status_code=401)
  else:
    raise HTTPException(detail={ 'message': 'Введены неверные данные.' }, status_code=401)