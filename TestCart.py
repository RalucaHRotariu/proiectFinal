import unittest

from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestCart(unittest.TestCase):
    LANDING_PAGE_URL = "https://www.decathlon.ro"
    EMAIL_SELECTOR = (By.ID, "input-email")
    PASSWORD_SELECTOR = (By.ID, "input-password")
    LOGIN_BUTTON = (By.ID, "lookup-btn")
    LOGGED_IN_USERNAME_ELEMENT = (By.CSS_SELECTOR, ".is-loggued.svelte-1xgh5x7 span.svelte-1xgh5x7")
    CART_COUNTER = (By.CSS_SELECTOR, ".count.svelte-3335j1")
    BINOCULARS_ITEM_URL = "https://www.decathlon.ro/p/binoclu-etans-900-10x42-kaki/_/R-p-327224?mc=8600097"
    CLOSE_DIALOG_BUTTON = (By.CSS_SELECTOR,
                           ".ecomm-sidepanel__overlay.svelte-1qm266f")
    ADD_TO_CART_BUTTON_CLASS = (By.CSS_SELECTOR, ".conversion-zone__purchase-cta")
    AGREE_TO_COOKIES_BUTTON = (By.ID, "didomi-notice-agree-button")
    CART_URL = "https://www.decathlon.ro/checkout/cart"
    DELETE_FROM_CART_BUTTON = (By.CSS_SELECTOR, "button.delete.svelte-1ajpw3q")

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")

        self.driver = webdriver.Chrome(options=chrome_options,
                                       service=Service())
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get(self.LANDING_PAGE_URL)

    def tearDown(self):
        self.driver.quit()

    def test_cart_empty(self):
        self.driver.get(self.LANDING_PAGE_URL)
        explict_wait = WebDriverWait(self.driver, 6)

        cart_counter_element = (
            explict_wait.until(EC.visibility_of_element_located(self.CART_COUNTER)))

        assert "0" in cart_counter_element.text, "Numarul de produse din cos este diferit de 0 dupa logare"

    def test_add_item_to_cart(self):
        self.driver.get(self.BINOCULARS_ITEM_URL)

        explict_wait = WebDriverWait(self.driver, 6)
        agree_to_cookies_button = (
            explict_wait.until(EC.visibility_of_element_located(self.AGREE_TO_COOKIES_BUTTON)))
        agree_to_cookies_button.click()

        add_to_cart_button = explict_wait.until(EC.visibility_of_element_located(self.ADD_TO_CART_BUTTON_CLASS))
        add_to_cart_button.click()

        close_dialog_button = explict_wait.until(EC.visibility_of_element_located(self.CLOSE_DIALOG_BUTTON))
        close_dialog_button.click()

        cart_counter_element = (
            explict_wait.until(EC.visibility_of_element_located(self.CART_COUNTER)))

        assert "1" in cart_counter_element.text, "Numarul de produse din cos nu este egal cu 1"

    def test_remove_from_cart(self):
        self.driver.get(self.BINOCULARS_ITEM_URL)

        explict_wait = WebDriverWait(self.driver, 6)
        agree_to_cookies_button = (
            explict_wait.until(EC.visibility_of_element_located(self.AGREE_TO_COOKIES_BUTTON)))
        agree_to_cookies_button.click()

        add_to_cart_button = explict_wait.until(EC.visibility_of_element_located(self.ADD_TO_CART_BUTTON_CLASS))
        add_to_cart_button.click()

        close_dialog_button = explict_wait.until(EC.visibility_of_element_located(self.CLOSE_DIALOG_BUTTON))
        close_dialog_button.click()

        self.driver.get(self.CART_URL)

        delete_from_cart_element = (
            explict_wait.until(EC.visibility_of_element_located(self.DELETE_FROM_CART_BUTTON)))
        delete_from_cart_element.click()

        self.driver.get(self.LANDING_PAGE_URL)

        cart_counter_element = (
            explict_wait.until(EC.visibility_of_element_located(self.CART_COUNTER)))

        assert "0" in cart_counter_element.text, "Numarul de produse din cos nu este egal cu 0"


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(TestCart('test_cart_empty'))
    suite.addTest(TestCart('test_add_item_to_cart'))
    suite.addTest(TestCart('test_remove_from_cart'))
    return suite


if __name__ == '__main__':
    runner = HTMLTestRunner(output='report',
                            combine_reports=True,
                            report_title='TestCart Results',
                            report_name='Automated Test Results')
    suite = test_suite()
    runner.run(suite)

