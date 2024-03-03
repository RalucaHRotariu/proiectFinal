import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from TestUtils import TestUtils


class TestsLogin(unittest.TestCase, TestUtils):
    LANDING_PAGE_URL = "https://www.decathlon.ro/login"
    EMAIL_SELECTOR = (By.ID, "input-email")
    PASSWORD_SELECTOR = (By.ID, "input-password")
    LOGIN_BUTTON = (By.ID, "lookup-btn")
    ALERT_ELEMENT = (By.CSS_SELECTOR, ".textfield-error-message[data-v-955c4fe4]")
    LOGGED_IN_USERNAME_ELEMENT = (By.CSS_SELECTOR, ".is-loggued.svelte-1xgh5x7 span.svelte-1xgh5x7")
    CONFIRM_BUTTON = (By.ID, "signin-button")

    def setUp(self):
        self.driver = TestUtils.setUp(self)

    def tearDown(self):
        TestUtils.tearDown(self)

    def test_login_incorrect_password(self):
        self.driver.get(self.LANDING_PAGE_URL)

        email_element = self.driver.find_element(*self.EMAIL_SELECTOR)
        password_element = self.driver.find_element(*self.PASSWORD_SELECTOR)
        login_button_element = self.driver.find_element(*self.LOGIN_BUTTON)

        self.driver.implicitly_wait(6.0)

        email_element.click()
        email_element.clear()
        email_element.send_keys("rotariu_ral@yahoo.com")

        login_button_element.click()

        password_element.click()
        password_element.clear()
        password_element.send_keys("SuperSecretPassword!")

        login_button_element.click()
        explict_wait = WebDriverWait(self.driver, 8)

        alert_element = explict_wait.until(EC.visibility_of_element_located(self.ALERT_ELEMENT))

        assert "Parolă incorectă" in alert_element.text, "Dupa parola invalida, mesajul nu este: parola incorecta!"

    def test_login_confirm_button_not_available(self):
        self.driver.get(self.LANDING_PAGE_URL)

        email_element = self.driver.find_element(*self.EMAIL_SELECTOR)
        password_element = self.driver.find_element(*self.PASSWORD_SELECTOR)
        login_button_element = self.driver.find_element(*self.LOGIN_BUTTON)

        self.driver.implicitly_wait(6.0)

        email_element.click()
        email_element.clear()
        email_element.send_keys("rotariu_ral@yahoo.com")

        login_button_element.click()

        password_element.click()
        password_element.clear()
        password_element.send_keys("Parola111")

        login_button_element.click()
        explict_wait = WebDriverWait(self.driver, 6)

        confirm_button_element = (
            explict_wait.until(EC.visibility_of_element_located(self.CONFIRM_BUTTON)))

        assert "true" in confirm_button_element.get_attribute("disabled"), "Butonul de confirmare nu este indisponibil!"

    def test_login_ok(self):
        self.driver.get(self.LANDING_PAGE_URL)

        email_element = self.driver.find_element(*self.EMAIL_SELECTOR)
        password_element = self.driver.find_element(*self.PASSWORD_SELECTOR)
        login_button_element = self.driver.find_element(*self.LOGIN_BUTTON)

        self.driver.implicitly_wait(6.0)

        email_element.click()
        email_element.clear()
        email_element.send_keys("rotariu_ral@yahoo.com")

        login_button_element.click()

        password_element.click()
        password_element.clear()
        password_element.send_keys("Parola111")

        login_button_element.click()
        explict_wait = WebDriverWait(self.driver, 8)

        logged_in_username_element = (
            explict_wait.until(EC.visibility_of_element_located(self.LOGGED_IN_USERNAME_ELEMENT)))

        assert "ROTARIU RALUCA" in logged_in_username_element.text, "Logarea nu s-a facut cu succes!"
