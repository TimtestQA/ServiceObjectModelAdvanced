import os
from client.api_client import RequestClient
from helpers.helper import Helper

class BaseAPI:

    client = RequestClient(base_url=os.environ["BASE_URL"])
    helper = Helper()