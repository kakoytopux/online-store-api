from fastapi import HTTPException, Request
from middlewares.db import db
from models.users import Users

def auth_admin(req: Request):
  session = db.get_session()

  get_user_info = session.query(Users).filter(Users.id == req.state.user['id']).first()
  session.close()

  if get_user_info.rank == 'admin':
    pass
  else:
    raise HTTPException(detail={ 'message': 'Недостаточно прав.' }, status_code=403)