from pages.webgeneric import webgeneric
from data.Testdata import *


class LoginPage(webgeneric):
    def __init__(self,driver):
        webgeneric. __init__(self,driver)
        self.un_id="username"
        self.pwd_name="pwd"
        self.login_button_id="loginButtonContainer"
        self.wg=webgeneric(driver)

    def login1(self,un,pwd):
        self.wg.enter("id",self.un_id,USERNAME)
        self.wg.enter("name",self.pwd_name,PASSWORD)
        self.wg.submit("xpath",self.login_button_id)



        # self.driver.find_element_by_id(self.un_id).send_keys("shivanpuneeth50@gmail.com")
        # self.driver.find_element_by_name(self.pwd_name).send_keys("manjushivu@1991")
        # self.driver.find_element_by_id(self.login_button_id).click()
