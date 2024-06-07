import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service

@pytest.fixture(scope="class")
def test_setup(request):
    options = Options()
    options.add_experimental_option("detach", True)
    service = Service('C:/Users/abinash.sahoo/Downloads/edgedriver_win64_ext/msedgedriver.exe')
    driver = webdriver.Edge(service=service, options=options)
    driver.maximize_window()
    request.cls.driver = driver
    return driver