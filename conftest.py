import pytest

from endpoints.login_endpoint import LoginEndpoint


@pytest.fixture()
def login_endpoint():
    return LoginEndpoint()
