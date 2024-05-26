import requests

from endpoints.base_endpoint import BaseEndpoint


class LoginEndpoint(BaseEndpoint):
    LOGIN_PATH = "api/Login"

    def login(self, payload: dict, headers=None):
        self.response = requests.post(
            url=f"{self.url}/{self.LOGIN_PATH}",
            json=payload,
            headers=headers if headers else self.headers,
        )
        self.json = self.response.json()
        return self.response
