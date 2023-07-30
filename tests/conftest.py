import pytest
from logic.client_logic import ClientLogic


def pytest_addoption(parser):
    parser.addoption("--username", action="store")
    parser.addoption("--password", action="store")


@pytest.fixture(name="test_client")
def client_for_test(request):
    client = ClientLogic(
        username=request.config.getoption("username"),
        password=request.config.getoption("password")
    )
    client.reset_table()
    return client
