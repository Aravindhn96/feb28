import pytest
from selenium import webdriver

@pytest.fixture(scope= "session")
def driver():
    driver = webdriver.Firefox()
    driver.get("https://practicetestautomation.com/practice-test-login/")

    yield driver
    driver.quit()