from fastapi import HTTPException
from fastapi.responses import JSONResponse

def exit_user(req):
  token = req.cookies.get('token')

  if token:
    res = JSONResponse(content='')
    res.set_cookie(key='token', expires=0)

    return res
  else:
    raise HTTPException(detail={ 'message': 'Куки не найден.' }, status_code=404)