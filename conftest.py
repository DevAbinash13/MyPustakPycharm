import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options

@pytest.fixture(scope="class")
def test_setup(request):
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Edge()
    driver.maximize_window()
    request.cls.driver = driver
    return driver