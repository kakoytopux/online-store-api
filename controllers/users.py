from operator import attrgetter
from models.user import User
from middlewares.db import db
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import bcrypt

def create_user(user):
  session = db.get_session()
  name, surname, age, email, password = attrgetter('name', 'surname', 'age', 'email', 'password')(user)

  hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
  
  try:
    new_user = User(name=name, surname=surname, age=age, email=email, password=hash)

    session.add(new_user)
    session.commit()

    session.refresh(new_user)
    session.close()

    json_res = jsonable_encoder(new_user)

    del json_res['password']

    return JSONResponse(content={ 'user': json_res }, status_code=201)
  except SQLAlchemyError as err:
    if(err.code == 'gkpj'):
      raise HTTPException(detail={ 'message': 'Такая почта уже используется.' }, status_code=409)
    if(err.code == '9h9h'):
      raise HTTPException(detail={ 'message': 'Введены некорректные данные.' }, status_code=400)
    
    raise HTTPException(detail={ 'message': 'Непредвиденная ошибка.' }, status_code=500)
  
def get_info_user(req):
  session = db.get_session()
  user = req.state.user

  try:
    get_user = select(User).where(User.email == user['email'])

    for user_obj in session.scalars(get_user):
      json_res = jsonable_encoder(user_obj)

      return JSONResponse(content={ 'user': json_res })
  except:
    raise HTTPException(detail={ 'message': 'Непредвиденная ошибка.' }, status_code=500)