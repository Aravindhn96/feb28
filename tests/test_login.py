import time

from pages.login_page import LoginPage
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

def test_invalid_login(driver):
    login_page = LoginPage(driver)
    username = config.get('login', "invalid_username")
    login_page.enter_username(username)
    password = config.get('login', 'invalid_password')
    login_page.enter_password(password)
    login_page.click_submit_button()
    assert login_page.login_unsuccesful("Your username is invalid!"), "Error message does not match or is missing"
    time.sleep(3)

def test_valid_login(driver):
    login_page = LoginPage(driver)
    username = config.get('login',"username")
    login_page.enter_username(username)
    password = config.get('login', 'password')
    login_page.enter_password(password)
    login_page.click_submit_button()
    assert login_page.login_succesful(), "login unsuccesful"
    time.sleep(3)
