from models.users import Users
from middlewares.db import db
from sqlalchemy import update
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import bcrypt

def get_data(data):
  data_obj = {}

  for key, value in data:
    if value:
      data_obj[key] = value
  
  return data_obj

def create_user(user):
  session = db.get_session()
  data_obj = get_data(user)

  try:
    data_obj['password'] = bcrypt.hashpw(data_obj['password'].encode('utf-8'), bcrypt.gensalt())
    sql = Users(**data_obj)

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
    user_obj = session.query(Users).filter(Users.id == req.state.user['id']).first()
    session.close()

    json_res = jsonable_encoder(user_obj)

    del json_res['password']

    return JSONResponse(content={ 'user': json_res })
  except:
    raise HTTPException(detail={ 'message': 'Непредвиденная ошибка.' }, status_code=500)
  
def change_user(req, user):
  session = db.get_session()

  data_obj = get_data(user)

  try:
    session.execute(update(Users).where(Users.id == req.state.user['id']).values(data_obj))
    session.commit()

    user_obj = session.query(Users).filter(Users.id == req.state.user['id']).first()
    session.close()

    json_res = jsonable_encoder(user_obj)

    del json_res['password']

    return JSONResponse(content={ 'user': json_res })
  except SQLAlchemyError as err:
    session.rollback()

    if(err.code == 'gkpj'):
      raise HTTPException(detail={ 'message': 'Такая почта уже используется.' }, status_code=409)
    
    raise HTTPException(detail={ 'message': 'Непредвиденная ошибка.' }, status_code=500)