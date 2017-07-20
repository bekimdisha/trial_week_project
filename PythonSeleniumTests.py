import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import logging 


class TestSignUpAndLogIn(unittest.TestCase):
	
    def setUp(self):
    # create a new Firefox session
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # navigate to the application home page
        self.driver.get("http://www.weebly.com/")
    
    def test_signup_new_user(self):
        # get the right url
        signup_url = self.driver.get("http://www.weebly.com#signup")

        signup_username = self.driver.find_element_by_id("overlay-signup-form-name")
        signup_username.send_keys("bekimdisha")
        time.sleep(1)
        signup_email = self.driver.find_element_by_id("overlay-signup-form-email")
        signup_email.send_keys("bekimdisha@gmail.com")
        time.sleep(1)
        signup_password = self.driver.find_element_by_id("overlay-signup-form-pass")
        signup_password.send_keys("!bekim123!")
        time.sleep(1)
        submit_button = self.driver.find_element_by_class_name("signup-form__submit")
        click_submit_button = self.driver.find_element_by_class_name("signup-form__submit").click()
        time.sleep(1)
        try:
        	not_now = self.driver.find_element_by_class_name("ecommerce-funnel__site-img")
        	chose_not_now = self.driver.find_element_by_class_name("ecommerce-funnel__site-img").click()
        except NoSuchElementException as eex:
            logging.info('test_signup_new_user FAILED', format(eex))
        time.sleep(1)
        try:
        	assert 'Weebly - Getting Started' in str(self.driver.title)
        except Exception as e:
        	logging.info('test_login FAILED', format(e))

    
    def test_login(self):

    	login_url = self.driver.get("http://www.weebly.com#login")

        username = self.driver.find_element_by_id("weebly-username")
        set_un = username.send_keys("bekimdisha@gmail.com")
        time.sleep(1)
        password = self.driver.find_element_by_id("weebly-password")
        set_pass = password.send_keys("!bekim123!")
        time.sleep(1)
        login_button = self.driver.find_element_by_class_name("login-btn")
        click_login_btn = self.driver.find_element_by_class_name("login-btn").click()
        time.sleep(1)

        try:
        	assert 'Weebly - Getting Started' in str(self.driver.title)
        except Exception as e:
        	logging.info('test_login FAILED', format(e))

    def tearDown(self):
    	self.driver.close()


if __name__ == '__main__':
    unittest.main()