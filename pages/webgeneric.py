from pages.LocatorGeneric import LocatorGeneric

class webgeneric(LocatorGeneric):
    def __init__(self,driver):
        LocatorGeneric.__init__(self,driver)


    def enter(self,locator_type,input_val,locator_val):
        var=self.locator(locator_type,locator_val)
        var.send_keys(input_val)
        # self.driver.find_element_by_id(locator).send_keys(input_val)



    def enter(self,locator_type,locator_val,input_val):
        var=self.locator(locator_type,locator_val)
        var.send_keys(input_val)
        # self.driver.find_element_by_name(locator).send_keys(input_val)

    def submit(self,locator_type,locator_val):
        var=self.locator(locator_type,locator_val)
        var.click()

        # self.driver.find_element_by_id(locator).click()







