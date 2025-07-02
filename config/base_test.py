# config/base_test.py (или где у тебя BaseTest)
import os

from services.users.api import UsersAPI
from services.cart.api import CartAPI
from config.tokens import TOKENS

class BaseTest:

    def setup_method(self):
        self.users_api = lambda role="default": UsersAPI(token=TOKENS[role])
        self.cart_api = lambda role="default": CartAPI(token=TOKENS[role])
