from pages.LoginPage import LoginPage
import pytest
from data.Testdata import *

# launch the browser and navigate to the URL
@pytest.mark.usefixtures("test_setup")
class Testlogincase:
    def test_login(self):
        driver=self.driver
        time=LoginPage(driver)
        time.login1(USERNAME,PASSWORD)


    # global driver




# homepage logout from the website
# def test_logout():
#     driver.implicitly_wait(30)
#     driver.find_element_by_xpath("//a[text()='Logout']").click()


