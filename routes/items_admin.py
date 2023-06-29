from fastapi import APIRouter
from middlewares.validator import CreateItem
from controllers.items_admin import create_item

router = APIRouter()

@router.post('/')
def get_create_item(item: CreateItem):
  return create_item(item)