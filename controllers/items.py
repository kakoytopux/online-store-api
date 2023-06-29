from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from models.items import Items
from middlewares.db import db

def get_items_all():
  session = db.get_session()

  try:
    sql = session.query(Items).all()
    session.close()

    json_res = jsonable_encoder(sql)

    return JSONResponse(content={ 'items': json_res })
  except:
    raise HTTPException(detail={ 'message': 'Непредвиденная ошибка.' }, status_code=500)