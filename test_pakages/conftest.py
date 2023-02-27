import pytest
from selenium import webdriver


@pytest.fixture()
def setUp1(browser):
    global driver
    if browser == 'ie':
        driver = webdriver.Ie()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")
