import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from POMDemo.pages.selectone_page import selectonePage

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(5)
    yield driver
    driver.close()
    driver.quit()

def test_selectone(driver):
    selectone_page = selectonePage(driver)
    selectone_page.selectone("https://trytestingthis.netlify.app/")
