import allure
import pytest
from config.base_test import BaseTest
from services.users.payloads import Payloads


@allure.epic("Users")
@allure.story("User list")
class TestUsers(BaseTest):

    @allure.title("Get list of all users")
    @pytest.mark.parametrize("offset, limit, success", [
        pytest.param(0, 10, True, id="valid offset and limit"),
        pytest.param(-10, 10, False, id="invalid offset"),
        pytest.param(0, -10, False, id="invalid limit"),
    ])
    @pytest.mark.users
    def test_user_list(self, offset, limit, success):
        self.users_api(role="admin").get_list_of_users(offset, limit, success)

    @allure.title("Create new user")
    @pytest.mark.parametrize("payload, success", [
        pytest.param(Payloads.create_user(), True, id="valid data"),
        pytest.param(Payloads.create_user_with_invalid_password(), False, id="invalid password"),
        pytest.param(Payloads.create_user_with_invalid_nickname(), False, id="invalid nickname"),
        pytest.param(Payloads.create_user_with_invalid_email(), False, id="invalid email"),
    ])
    @pytest.mark.users
    def test_create_user(self, payload, success):
        self.users_api(role="admin").create_user(payload, success)






