from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.ID, "username").send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, "password").send_keys(password)

    def click_submit_button(self):
        self.driver.find_element(By.ID, "submit").click()

    def login_succesful(self):
        title = self.driver.title
        return title == "Logged In Successfully | Practice Test Automation"

    def get_error_message(self):
        try:
            error_element = self.driver.find_element(By.ID, "error")
            return error_element.text
        except NoSuchElementException:
            return None

    def login_unsuccesful(self, expected_message):
        actual_message = self.get_error_message()
        if actual_message is None:
            return False
        return actual_message == expected_message






    


