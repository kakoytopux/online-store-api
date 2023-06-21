from fastapi import HTTPException, Request
import jwt
import os

def auth(req: Request):
  token = req.cookies.get('token')

  if token:
    try:
      req.state.user = jwt.decode(token, os.getenv('SECRET_KEY') if os.getenv('MODE') == 'production' else 'secret-dev', algorithms=['HS256'])

      return req
    except:
      raise HTTPException(detail={ 'message': 'Необходимо пройти авторизацию.' }, status_code=401)
  else:
    raise HTTPException(detail={ 'message': 'Необходимо пройти авторизацию.' }, status_code=401)