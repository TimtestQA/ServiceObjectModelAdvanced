import allure
from config.base_api import BaseAPI
from config.headers import Headers
from services.cart.endpoints import Endpoints
from services.cart.payloads import Payloads
from services.cart.models.model_add_item import AddCartResponseModel

class CartAPI(BaseAPI):
    def __init__(self, token: str, auth_type: str = "bearer", base_url: str = None):
        self.headers = Headers(token=token, auth_type=auth_type)
        self.endpoints = Endpoints()
        self.payloads = Payloads()

    @allure.step("Add item to cart")
    def add_item_to_cart(self, user_id, payload, success: bool = True):
        response = self.client.post(
            model=AddCartResponseModel,
            endpoint=self.endpoints.add_item(user_id),
            json=payload,
            headers=self.headers.get(),
            success=success
        )
        return response
