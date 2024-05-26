import allure
import pytest


@pytest.mark.regression
@allure.feature("Common user's actions")
@allure.story("Send a valid Delete_meme request")
@allure.title("Test for a DELETE request")
def test_login(login_endpoint):
    payload = {"username": "ugabuga", "password": "123456Zz"}

    login_endpoint.login(payload=payload)
    login_endpoint.validate_status_code_is_200()
