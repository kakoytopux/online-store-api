from fastapi import HTTPException, Request
import jwt

async def auth(req: Request):
  token = req.cookies.get('token')

  if token:
    try:
      req.state.user = jwt.decode(token, 'secret-dev', algorithms=['HS256'])

      return req
    except:
      raise HTTPException(detail={ 'message': 'Необходимо пройти авторизацию.' }, status_code=401)
  else:
    raise HTTPException(detail={ 'message': 'Необходимо пройти авторизацию.' }, status_code=401)