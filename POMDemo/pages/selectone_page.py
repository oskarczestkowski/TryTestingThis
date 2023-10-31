import time

from selenium.webdriver.common.by import By


class selectonePage:
    def __init__(self, driver):
        self.driver = driver
        self.selectone_locator = (By.ID, "option")
        self.selectone_option = [By.XPATH, "/html/body/div[3]/div[2]/form/fieldset/select[1]/option[3]"]

    def selectone(self,url):
        self.driver.get(url)
        self.driver.find_element(*self.selectone_locator).click()
        self.driver.find_element(*self.selectone_option).click()
