from selenium.webdriver.common.by import By


class genderPage:
    def __init__(self, driver):
        self.driver = driver
        self.gender_radiobutton = (By.ID, "male")

    def gender(self,url):
        self.driver.get(url)
        self.driver.find_element(*self.gender_radiobutton).click()
