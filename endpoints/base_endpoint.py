from typing import Optional, Dict, Any

import allure
import requests
from pydantic import BaseModel, ValidationError


class BaseEndpoint:
    url: str = "https://bookcart.azurewebsites.net"
    response: Optional[requests.Response] = None
    json: Optional[Dict[str, Any]] = None
    token: str = None
    headers: Dict[str, str] = {"Content-type": "application/json"}

    @allure.step("Validate response data according to a model")
    def validate_response(self, response_model: type[BaseModel]) -> None:
        if self.json is None:
            raise AssertionError("No data in JSON.")
        try:
            response_model.model_validate(self.json)
        except ValidationError as e:
            raise AssertionError(f"Validation error: {e}")

    @allure.step("Validate that status code is 200")
    def validate_status_code_is_200(
        self, error_message="Status code isn't 200"
    ) -> None:
        assert self.response.status_code == 200, error_message
