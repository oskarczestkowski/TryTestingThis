from selenium.webdriver.common.by import By


class flnamePage:
    def __init__(self, driver):
        self.driver = driver
        self.fname_textbox = (By.ID, "fname")
        self.lname_textbox = (By.ID, "lname")

    def flname(self, url, fname, lname):
        self.driver.get(url)
        self.driver.find_element(*self.fname_textbox).send_keys(fname)
        self.driver.find_element(*self.lname_textbox).send_keys(lname)