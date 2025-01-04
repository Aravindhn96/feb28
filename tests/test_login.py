from pages.login_page import LoginPage
import time
import configparser
import logging

config = configparser.ConfigParser()
config.read("config.ini")
logging.basicConfig(filename="test.log", level=logging.DEBUG)

def test_validlogin(driver):
    login_page = LoginPage(driver)
    logging.info("Starting the testcase - Test Valid login")
    username = config.get("login", "username")
    login_page.enter_username(username)
    logging.info("entering the username")
    password = config.get("login", "password")
    login_page.enter_password(password)
    logging.info("entering the password")
    login_page.click_submit_button()
    logging.info("Click submit button")
    expected_url = "https://practicetestautomation.com/logged-in-successfully/"
    actual_url = driver.current_url
    assert actual_url == expected_url

def test_invalidlogin():
    print("hello")
    print("hello")

def test_verify_contacts_page():
    pass





