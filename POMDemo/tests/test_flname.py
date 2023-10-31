import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from POMDemo.pages.flname_page import flnamePage

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(5)
    yield driver
    driver.close()
    driver.quit()

def test_flname(driver):
    flname_page = flnamePage(driver)
    flname_page.flname("https://trytestingthis.netlify.app","Oskar","Czestkowski")


