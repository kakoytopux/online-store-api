from fastapi import APIRouter, Request
from controllers.items import set_like_item, get_items_all

router = APIRouter()

@router.get('/')
def get_items():
  return get_items_all()

@router.patch('/like/{id}')
def get_item_like(req: Request, id: int):
  return set_like_item(req, id)