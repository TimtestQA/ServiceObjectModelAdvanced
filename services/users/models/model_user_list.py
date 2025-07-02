from typing import List
from pydantic import BaseModel

class Meta(BaseModel):
    total: int

class User(BaseModel):
    email: str
    name: str
    nickname: str
    avatar_url: str
    uuid: str

class UserListResponseModel(BaseModel):
    meta: Meta
    users: List[User]
