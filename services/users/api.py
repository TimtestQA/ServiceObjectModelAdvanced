import allure
from config.base_api import BaseAPI
from config.headers import Headers
from services.users.endpoints import Endpoints
from services.users.payloads import Payloads
from services.users.models.model_user_list import UserListResponseModel
from services.users.models.model_user import UserResponseModel

class UsersAPI(BaseAPI):
    def __init__(self, token: str, auth_type: str = "bearer", base_url: str = None):
        self.headers = Headers(token=token, auth_type=auth_type)
        self.endpoints = Endpoints()
        self.payloads = Payloads()

    @allure.step("Get list of users")
    def get_list_of_users(self, offset: int = 0, limit: int = 10, success: bool = True):
        response = self.client.get(
            model=UserListResponseModel,
            endpoint=self.endpoints.list_all_users,
            params={"offset": offset, "limit": limit},
            headers=self.headers.get(),
            success=success
        )
        return response

    @allure.step("Create user")
    def create_user(self, payload=None, success=True) -> UserResponseModel:
        response = self.client.post(
            model=UserResponseModel,
            endpoint=self.endpoints.create_user,
            json=payload or Payloads.create_user(),
            headers=self.headers.get(),
            success=success
        )
        return response