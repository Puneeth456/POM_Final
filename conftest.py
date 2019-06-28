import pytest
from data.Testdata import *



@pytest.fixture(scope='class')
def test_setup(request):
    from selenium import webdriver
    driver=webdriver.Chrome(executable_path="C:/Users/Admin/Downloads/chromedriver.exe")
    driver.get(URL)
    driver.implicitly_wait(20)
    request.cls.driver=driver

