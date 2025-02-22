import pytest
from selenium import webdriver

@pytest.fixture(scope= "session")
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://practicetestautomation.com/practice-test-login/")

    yield driver
    driver.quit()

