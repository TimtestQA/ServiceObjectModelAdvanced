import base64
from typing import Optional, Dict


class Headers:
    def __init__(self,
                 token: Optional[str] = None,
                 auth_type: str = "bearer",
                 extra_headers: Optional[Dict[str, str]] = None):
        self.token = token
        self.auth_type = auth_type.lower()
        self.extra_headers = extra_headers or {}

    def get(self) -> dict:
        headers = {
            "Content-Type": "application/json",
            "x-task-id": "api-1",
        }

        if self.token:
            if self.auth_type == "bearer":
                headers["Authorization"] = f"Bearer {self.token}"
            elif self.auth_type == "api-key":
                headers["x-api-key"] = self.token
            elif self.auth_type == "basic":
                encoded_token = base64.b64encode(self.token.encode()).decode()
                headers["Authorization"] = f"Basic {encoded_token}"
            else:
                raise ValueError(f"Unknown auth_type: {self.auth_type}")

        headers.update(self.extra_headers)
        return headers

