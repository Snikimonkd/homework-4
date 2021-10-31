class Component(object):
    def __init__(self, driver):
        self.driver = driver

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()
