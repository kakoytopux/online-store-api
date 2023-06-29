from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from models.items import Items
from middlewares.db import db

def get_data(data):
  data_obj = {}

  for key, value in data:
    if value:
      data_obj[key] = value
  
  return data_obj

def create_item(item):
  session = db.get_session()
  data_obj = get_data(item)

  try:
    sql = Items(**data_obj)

    session.add(sql)
    session.commit()

    session.refresh(sql)
    session.close()

    json_res = jsonable_encoder(sql)

    return JSONResponse(content={ 'item': json_res })
  except:
    raise HTTPException(detail={ 'message': 'Непредвиденная ошибка.' }, status_code=500)