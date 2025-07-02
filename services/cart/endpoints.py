import os


class Endpoints:

    get_cart = lambda self, user_id: f"/users/{user_id}/cart"
    add_item = lambda self, user_id: f"/users/{user_id}/cart/add"
