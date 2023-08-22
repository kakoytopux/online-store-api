from fastapi import APIRouter, Request
from controllers.items import set_like_item, get_liked_items, delete_like_item

router = APIRouter()

@router.patch('/like/{id}')
def get_item_like(req: Request, id: int):
  return set_like_item(req, id)

@router.delete('/like/{id}')
def get_delete_like_item(req: Request, id: int):
  return delete_like_item(req, id)

@router.get('/like')
def return_liked_items(req: Request):
  return get_liked_items(req)