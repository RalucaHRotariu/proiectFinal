import time
import unittest

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestsLogin(unittest.TestCase):
    LANDING_PAGE_URL = "https://www.decathlon.ro/login"
    CART_COUNTER = (By.CSS_SELECTOR, ".count.svelte-3335j1")
    BINOCULARS_ITEM_URL = "https://www.decathlon.ro/p/binoclu-etans-900-10x42-kaki/_/R-p-327224?mc=8600097"
    AGREE_TO_COOKIES_BUTTON = (By.ID, "didomi-notice-agree-button")
    FAVORITES_COUNTER = (By.CSS_SELECTOR, "span.indicator.svelte-15albxt")
    ADD_TO_FAVORITES_BUTTON = (By.XPATH,
                               "/html/body/div[2]/main/article/div/div[2]/section/div[4]/div/button[2]")
    SEE_FAVORITES_BUTTON = (By.XPATH,
                            "/html/body/div[2]/header/div[1]/nav/div[2]/div[1]/div/button")
    CLOSE_FAVORITES_DIALOG = (By.XPATH,
                              "/html/body/div[3]/div/div[2]/div[1]/button/span")
    DIALOG_ADD_TO_CART_BUTTON = (By.XPATH,
                                 "/html/body/div[3]/div/div[2]/div[2]/p/div/section/div/article/div[3]/div/button[1]")

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

    def test_favorites_empty(self):
        self.driver.get(self.BINOCULARS_ITEM_URL)

        explict_wait = WebDriverWait(self.driver, 6)
        try:
            agree_to_cookies_button = (
                explict_wait.until(EC.visibility_of_element_located(self.AGREE_TO_COOKIES_BUTTON)))
            agree_to_cookies_button.click()

        except NoSuchElementException:
            print("AGREE_TO_COOKIES_BUTTON not found")

        favorites_counter_element = (
            explict_wait.until(EC.visibility_of_element_located(self.FAVORITES_COUNTER)))

        assert "0" in favorites_counter_element.text, "Numarul de produse Favorite este diferit de 0"

    def test_add_item_to_favorites(self):
        self.driver.get(self.BINOCULARS_ITEM_URL)

        explict_wait = WebDriverWait(self.driver, 6)
        try:
            agree_to_cookies_button = (
                explict_wait.until(EC.visibility_of_element_located(self.AGREE_TO_COOKIES_BUTTON)))
            agree_to_cookies_button.click()

        except NoSuchElementException:
            print("AGREE_TO_COOKIES_BUTTON not found. Continue")

        add_to_favorites_button = (
            explict_wait.until(EC.visibility_of_element_located(self.ADD_TO_FAVORITES_BUTTON)))
        add_to_favorites_button.click()

        time.sleep(20)

        favorites_counter_element = (
            explict_wait.until(EC.visibility_of_element_located(self.FAVORITES_COUNTER)))

        assert "1" in favorites_counter_element.text, "Numarul de produse Favorite este diferit de 1"

    def test_remove_item_from_favorites(self):
        self.driver.get(self.BINOCULARS_ITEM_URL)

        explict_wait = WebDriverWait(self.driver, 6)
        try:
            agree_to_cookies_button = (
                explict_wait.until(EC.visibility_of_element_located(self.AGREE_TO_COOKIES_BUTTON)))
            agree_to_cookies_button.click()

        except NoSuchElementException:
            print("AGREE_TO_COOKIES_BUTTON not found. Continue")

        add_to_favorites_button = (
            explict_wait.until(EC.visibility_of_element_located(self.ADD_TO_FAVORITES_BUTTON)))
        add_to_favorites_button.click()

        time.sleep(20)

        add_to_favorites_button.click()

        time.sleep(20)

        favorites_counter_element = (
            explict_wait.until(EC.visibility_of_element_located(self.FAVORITES_COUNTER)))

        assert "0" in favorites_counter_element.text, "Numarul de produse Favorite este diferit de 0"

    def test_move_from_favorites_to_Cart(self):
        self.driver.get(self.BINOCULARS_ITEM_URL)

        explict_wait = WebDriverWait(self.driver, 6)
        try:
            agree_to_cookies_button = (
                explict_wait.until(EC.visibility_of_element_located(self.AGREE_TO_COOKIES_BUTTON)))
            agree_to_cookies_button.click()

        except NoSuchElementException:
            print("AGREE_TO_COOKIES_BUTTON not found. Continue")

        add_to_favorites_button = (
            explict_wait.until(EC.visibility_of_element_located(self.ADD_TO_FAVORITES_BUTTON)))
        add_to_favorites_button.click()

        time.sleep(20)

        see_favorites_button = (
            explict_wait.until(EC.visibility_of_element_located(self.SEE_FAVORITES_BUTTON)))
        see_favorites_button.click()

        time.sleep(5)

        dialog_add_to_cart_button = (
            explict_wait.until(EC.visibility_of_element_located(self.DIALOG_ADD_TO_CART_BUTTON)))
        dialog_add_to_cart_button.click()

        time.sleep(10)

        close_favorites_dialog = (
            explict_wait.until(EC.visibility_of_element_located(self.CLOSE_FAVORITES_DIALOG)))
        close_favorites_dialog.click()

        time.sleep(5)

        favorites_counter_element = (
            explict_wait.until(EC.visibility_of_element_located(self.FAVORITES_COUNTER)))

        cart_counter_element = (
            explict_wait.until(EC.visibility_of_element_located(self.CART_COUNTER)))

        time.sleep(5)

        assert "0" in favorites_counter_element.text, "Numarul de produse Favorite este diferit de 0"
        assert "1" in cart_counter_element.text, "Numarul de produse din cos nu este egal cu 1"


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(TestsLogin('test_favorites_empty'))
    suite.addTest(TestsLogin('test_add_item_to_favorites'))
    suite.addTest(TestsLogin('test_remove_item_from_favorites'))
    suite.addTest(TestsLogin('test_move_from_favorites_to_Cart'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    suite = test_suite()
    result = runner.run(suite)
