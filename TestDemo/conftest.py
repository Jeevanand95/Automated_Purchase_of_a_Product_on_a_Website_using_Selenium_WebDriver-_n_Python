import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#
# def pytest_parser(parser):
#     parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    # browser_name = request.config.getoption("--browser_name")
    # if browser_name == "chrome":
    #     driver = webdriver.Chrome(executable_path="C:\\Driver\\chromedriver.exe")
    #     driver.get("https://rahulshettyacademy.com/angularpractice/")
    # elif browser_name == "firefox":
    #     driver = webdriver.Firefox(executable_path="C:\Driver\geckodriver.exe")
    #     driver.get("https://rahulshettyacademy.com/angularpractice/")
    # # elif browser_name == "edge":
    # #     driver = webdriver.Edge()
    # #     driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    driver.close()
