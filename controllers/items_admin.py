from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from models.items import Items
from middlewares.db import db
from sqlalchemy import update, delete

def get_data(data):
  data_obj = {}

  for key, value in data:
    if value:
      data_obj[key] = value
  
  return data_obj

def create_item(data):
  session = db.get_session()
  data_obj = get_data(data)

  try:
    sql = Items(**data_obj)

    session.add(sql)
    session.commit()

    session.refresh(sql)
    session.close()

    json_res = jsonable_encoder(sql)

    return JSONResponse(content={ 'item': json_res })
  except:
    session.rollback()

    raise HTTPException(detail={ 'message': 'Непредвиденная ошибка.' }, status_code=500)
  
def edit_item(data, id):
  session = db.get_session()
  data_obj = get_data(data)

  try:
    session.execute(update(Items).where(Items.id == id).values(data_obj))
    session.commit()

    sql = session.query(Items).get(id)
    session.close()

    json_res = jsonable_encoder(sql)

    return JSONResponse(content={ 'item': json_res })
  except:
    raise HTTPException(detail={ 'message': 'Непредвиденная ошибка.' }, status_code=500)
  
def delete_item(id):
  session = db.get_session()

  try:
    item_obj = session.query(Items).get(id)
    session.close()

    if item_obj == None:
      return JSONResponse(content={ 'message': 'Товар не найден.' }, status_code=404)
    
    session.execute(delete(Items).where(Items.id == id))
    session.commit()

    json_res = jsonable_encoder(item_obj)

    return JSONResponse(content={ 'item': json_res })
  except:
    session.rollback()
    
    raise HTTPException(detail={ 'message': 'Непредвиденная ошибка.' }, status_code=500)