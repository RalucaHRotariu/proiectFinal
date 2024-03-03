import time
import unittest

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from TestUtils import TestUtils


class TestsFavorites(unittest.TestCase, TestUtils):
    LANDING_PAGE_URL = "https://www.decathlon.ro"
    CART_COUNTER = (By.CSS_SELECTOR, ".count.svelte-3335j1")
    BINOCULARS_ITEM_URL = "https://www.decathlon.ro/p/binoclu-etans-900-10x42-kaki/_/R-p-327224?mc=8600097"
    AGREE_TO_COOKIES_BUTTON = (By.ID, "didomi-notice-agree-button")
    FAVORITES_COUNTER = (By.CSS_SELECTOR, "span.indicator.svelte-15albxt")
    ADD_TO_FAVORITES_BUTTON = (By.XPATH, "//div[4]/div/button[2]")
    SEE_FAVORITES_BUTTON = (By.XPATH, "//nav/div[2]/div[1]/div/button")
    CLOSE_FAVORITES_DIALOG = (By.XPATH, "//div[2]/div[1]/button/span")
    DIALOG_ADD_TO_CART_BUTTON = (By.XPATH, "//article/div[3]/div/button[1]")

    def setUp(self):
        self.driver = TestUtils.setUp(self)

    def tearDown(self):
        TestUtils.tearDown(self)

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
