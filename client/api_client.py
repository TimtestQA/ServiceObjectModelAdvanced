import requests
import allure
from utils.logger import logger
from pydantic import BaseModel
from config.headers import Headers
from helpers.helper import Helper


class RequestClient:

    def __init__(self, base_url, headers=None):
        self.helper = Helper()
        self.base_url = base_url  # https://example.com/api/v1
        self.session = requests.Session()

        # Устанавливаем базовые headers по умолчанию
        default_headers = Headers().get()
        self.session.headers.update(default_headers)

        # Если переданы дополнительные headers, объединяем их с дефолтными
        if headers:
            self.session.headers.update(headers)

    def _log_request(self, method, url, **kwargs):
        logger.info(f"➡️ {method.upper()} - {url}")
        if "json" in kwargs and method.upper() != "GET":
            self.helper.attach("request", kwargs["json"])

    def _log_response(self, response: requests.Response):
        logger.info(f"⬅️ Status: {response.status_code}")
        logger.info(f"Response: {response.json()}")

    def _request(self, method, endpoint, headers=None, success = None, **kwargs) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        self._log_request(method, url, **kwargs)

        if success:
            # Используем сессию, если headers указаны для конкретного запроса — добавляем их
            response = self.session.request(method=method, url=url, headers=headers, **kwargs)
            assert 200 <= response.status_code < 400, response.json()
        else:
            try:
                response = self.session.request(method=method, url=url, headers=headers, **kwargs)
                assert response.status_code >= 400, response.json()
            except:
                pass
        self._log_response(response)
        return response

    def _validate_response(self, response: requests.Response, model: type[BaseModel], status_code: int = 200):
        self.helper.attach("response", response.json())
        assert response.status_code == status_code, response.json()
        if isinstance(response.json(), dict):
            return model(**response.json())
        elif isinstance(response.json(), list):
            return [model(**item) for item in response.json()]

    def get(self, model, endpoint, params=None, headers=None, success = True) -> None | BaseModel | list[BaseModel]:
        response = self._request("get", endpoint, params=params, headers=headers, success=success)
        if success:
            return self._validate_response(model=model, response=response)
        else:
            pass

    def post(self, model, endpoint, json=None, headers=None, success=None) -> None | BaseModel | list[BaseModel]:
        response = self._request("post", endpoint, json=json, headers=headers)
        if success:
            return self._validate_response(model=model, response=response)
        else:
            pass

    def patch(self, model, endpoint, json=None, headers=None, success=True) -> None | BaseModel | list[BaseModel]:
        response = self._request("patch", endpoint, json=json, headers=headers)
        if success:
            return self._validate_response(model=model, response=response)
        else:
            pass

    def delete(self, model, endpoint, headers=None, success=True) -> requests.Response:
        if success:
            return self._validate_response(model=model, response=response)
        else:
            pass










