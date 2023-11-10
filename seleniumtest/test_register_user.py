import unittest
from selenium.webdriver.common.by import By
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class AuthenticationTestCase(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        #firefox_options = webdriver.FirefoxOptions()
        #firefox_options.add_argument('--headless')

        # Use headless Firefox
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("http://172.17.0.2:5000/register/")
    def test_registration(self):
        username = "abc"
        email = "abc@gmail.com"
        password = "K95SiBeFftjQNLt"

        # Find the input fields and the registration button
        username_input = self.driver.find_element(By.ID, "username")
        email_input = self.driver.find_element(By.ID, "email")
        password_input = self.driver.find_element(By.ID, "pwd")
        conform_password_input = self.driver.find_element(By.ID, "cpwd")
        register_button = self.driver.find_element(By.CLASS_NAME, "btn")

        # Fill in the registration form
        username_input.send_keys(username)
        email_input.send_keys(email)
        password_input.send_keys(password)
        conform_password_input.send_keys(password)

        # Click the registration button
        register_button.click()

        # Check for success message
        try:
            success_msg = self.driver.find_element(By.CLASS_NAME, "alert-success")
            message_text = success_msg.get_attribute("innerHTML")
            message_text_only = re.sub(r'<.*?>', '', message_text)
            expected_alarm_msg = "Account Succesfully created"
            self.assertEqual(message_text_only.strip(), expected_alarm_msg)

        except:
            # If no success message is found, check for the error message
            error_msg = self.driver.find_element(By.CLASS_NAME, "alert-warning")
            message_text = error_msg.get_attribute("innerHTML")
            message_text_only = re.sub(r'<.*?>', '', message_text)
            expected_alarm_msg =  'User already exists!.' if 'User' in  message_text_only.strip() else  'Email already registered!'
            self.assertEqual(message_text_only.strip(), expected_alarm_msg)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
