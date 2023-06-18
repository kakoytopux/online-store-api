from operator import attrgetter
from models.user import User
from middlewares.db import db
from sqlalchemy import select, update
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
    sql = User(name=name, surname=surname, age=age, email=email, password=hash)

    session.add(sql)
    session.commit()

    session.refresh(sql)
    session.close()

    json_res = jsonable_encoder(sql)

    del json_res['password']

    return JSONResponse(content={ 'user': json_res }, status_code=201)
  except SQLAlchemyError as err:
    if(err.code == 'gkpj'):
      raise HTTPException(detail={ 'message': 'Такая почта уже используется.' }, status_code=409)
    if(err.code == '9h9h'):
      raise HTTPException(detail={ 'message': 'Введены некорректные данные.' }, status_code=400)
    
    raise HTTPException(detail={ 'message': 'Непредвиденная ошибка.' }, status_code=500)
  
def get_user_info(req):
  session = db.get_session()
  
  try:
    for user_obj in session.scalars(select(User).where(User.email == req.state.user['email'])):
      json_res = jsonable_encoder(user_obj)

      del json_res['password']

      return JSONResponse(content={ 'user': json_res })
    
    session.close()
  except:
    raise HTTPException(detail={ 'message': 'Непредвиденная ошибка.' }, status_code=500)
  
def get_user_changed(req, user):
  session = db.get_session()

  data_obj = {}

  for key, value in user:
    if value:
      data_obj[key] = value 

  try:
    sql = update(User).where(User.email == req.state.user['email']).values(data_obj)

    session.execute(sql)
    session.commit()

    return JSONResponse(content={ 'user': 'ok' })
  except:
    raise HTTPException(detail={ 'message': 'Непредвиденная ошибка.' }, status_code=500)