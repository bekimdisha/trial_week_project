import os
from selenium import webdriver
cd = "/usr/local/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = cd 
driver = webdriver.Chrome(cd)
driver.get("http://www.weebly.com#signup")
signup_form_input = driver.find_element_by_id("overlay-signup-form-name")
signup_form_input.send_keys("bekimdisha")
signup_form_input = driver.find_element_by_id("overlay-signup-form-email")
signup_form_input.send_keys("bekimdisha@gmail.com")
signup_form_input = driver.find_element_by_id("overlay-signup-form-pass")
signup_form_input.send_keys("!bekim123!")
submit_button = driver.find_element_by_class_name("signup-form__submit")
click_submit_button = driver.find_element_by_class_name("signup-form__submit").click()
not_now = driver.find_element_by_class_name("ecommerce-funnel__site-img")
chose_not_now = driver.find_element_by_class_name("ecommerce-funnel__site-img").click()

#you get the point. 
driver.quit()