import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):

    # browser = request.config.getoption("--browser")

    # match browser:
    #     case 'chrome':
    #         driver = webdriver.Chrome()
    #     case 'firefox':
    #         driver = webdriver.Firefox()
    #     case 'edge':
    #         driver = webdriver.Edge()

    driver = webdriver.Chrome()
    # driver.get("http://192.168.20.15:81/peza/login")
    driver.get("http://192.168.20.15:81/peza-v2/login")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

# def pytest_addoption(parser):
#     parser.addoption("--browser", action="store", default="chrome", help="Specify the browser: chrome or firefox")


@pytest.fixture(scope="class")
def ecp_setup(request):
    driver = webdriver.Chrome()
    driver.get("http://112.199.119.250:88/ECP/auth/login")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


# def pytest_addoption(parser):
#     parser.addoption("--browser")
#
#
# @pytest.fixture(scope="class", autouse=True)
# def browser(request):
#     return request.config.getoption("--browser")
