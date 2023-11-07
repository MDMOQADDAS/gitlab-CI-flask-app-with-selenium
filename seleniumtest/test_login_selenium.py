import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class AuthenticationTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://127.0.0.1:5000/login")

    def test_login_with_valid_credentials(self):
        email = "a@gmail.com"
        password = "J75SiBnFftjQNLz"

        # Find the email and password input fields and the login button
        email_input = self.driver.find_element(By.ID,"email")
        password_input = self.driver.find_element(By.ID,"pwd")
        login_button = self.driver.find_element(By.CLASS_NAME, "btn")

        # Enter the email and password
        email_input.send_keys(email)
        password_input.send_keys(password)

        # Click the login button
        login_button.click()

        # Check if the user is redirected to the expected page after login
        expected_url = "http://127.0.0.1:5000/"
        self.assertEqual(self.driver.current_url, expected_url)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

