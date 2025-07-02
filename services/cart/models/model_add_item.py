from typing import List
from uuid import UUID
from pydantic import BaseModel

class CartItem(BaseModel):
    item_uuid: UUID
    quantity: int
    total_price: int

class AddCartResponseModel(BaseModel):
    items: List[CartItem]
    total_price: int
    user_uuid: UUID