from fastapi import APIRouter
from middlewares.validator import CreateItem, EditItem
from controllers.items_admin import create_item, edit_item, delete_item

router = APIRouter()

@router.post('/')
def get_create_item(data: CreateItem):
  return create_item(data)

@router.patch('/{id}')
def get_edit_item(data: EditItem, id: int):
  return edit_item(data, id)

@router.delete('/{id}')
def get_delete_item(id: int):
  return delete_item(id)