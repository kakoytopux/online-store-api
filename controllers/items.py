from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy import update
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

def set_like_item(req, id):
  session = db.get_session()

  try:
    item_obj = session.query(Items).get(id)

    if item_obj == None:
      return JSONResponse(content={ 'message': 'Товар не найден.' }, status_code=404)

    if item_obj.likes['users_id'].count(req.state.user['id']):
      return JSONResponse(content={ 'message': 'Данный пользователь уже поставил лайк.' }, status_code=409)

    item_obj.likes['users_id'].append(req.state.user['id'])

    json_res = jsonable_encoder(item_obj)

    session.execute(update(Items).where(Items.id == id).values(likes=item_obj.likes))
    session.commit()

    return JSONResponse(content={ 'item': json_res })
  except:
    raise HTTPException(detail={ 'message': 'Непредвиденная ошибка.' }, status_code=500)
  
def delete_like_item(req, id):
  session = db.get_session()

  try:
    item_obj = session.query(Items).get(id)

    if item_obj == None:
      return JSONResponse(content={ 'message': 'Товар не найден.' }, status_code=404)

    if 'users_id' not in item_obj.likes:
      item_obj.likes = { 'users_id': [] }

    if not item_obj.likes['users_id'].count(req.state.user['id']):
      return JSONResponse(content={ 'message': 'Пользователь не найден.' }, status_code=404)

    item_obj.likes['users_id'].remove(req.state.user['id'])

    json_res = jsonable_encoder(item_obj)

    session.execute(update(Items).where(Items.id == id).values(likes=item_obj.likes))
    session.commit()

    return JSONResponse(content={ 'item': json_res })
  except:
    raise HTTPException(detail={ 'message': 'Непредвиденная ошибка.' }, status_code=500)

def get_liked_items(req):
  session = db.get_session()

  try:
    sql = session.query(Items).where(Items.likes['users_id']).all()
    session.close()

    items_obj = []

    for item in sql:
      if item.likes['users_id'].count(req.state.user['id']):
        items_obj.append(item)

    json_res = jsonable_encoder(items_obj)

    return JSONResponse(content={ 'items': json_res })
  except:
    raise HTTPException(detail={ 'message': 'Непредвиденная ошибка.' }, status_code=500)