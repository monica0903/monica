from selenium.webdriver.common.by import By

class FinancePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.google.com/finance")
        self.may_be_interested_by = (By.XPATH, "//ul[@class='sbnBtf']/li/a//div[@class='COaKTb']")
        self.title = self.driver.title

    def get_may_be_interested_in(self):
        return self.driver.find_elements(self.may_be_interested_by[0], self.may_be_interested_by[1])

    def get_may_be_interested_in_text(self):
        return [x.text for x in self.get_may_be_interested_in()]