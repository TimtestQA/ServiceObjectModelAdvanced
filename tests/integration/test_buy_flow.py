import allure
import pytest
from config.base_test import BaseTest
from services.cart.payloads import Payloads


@allure.epic("Purchase")
@allure.story("Buy")
class TestBuyFlow(BaseTest):

    @allure.title("Add item to cart")
    @pytest.mark.buy_flow
    @pytest.mark.parametrize("item_payload, success", [
        pytest.param(Payloads.add_item(), True, id="valid data"),
        pytest.param(Payloads.add_item_with_invalid_quantity(), False, id="invalid quantity"),
    ])
    def test_add_item_to_cart(self, item_payload, success):
        user = self.users_api(role="admin").create_user()
        self.cart_api(role="admin").add_item_to_cart(user.uuid, item_payload, success)