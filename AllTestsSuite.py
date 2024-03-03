from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


class TestUtils:
    LANDING_PAGE_URL = "https://www.decathlon.ro"

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")

        self.driver = webdriver.Chrome(options=chrome_options,
                                       service=Service())
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get(self.LANDING_PAGE_URL)

        return self.driver

    def tearDown(self):
        self.driver.quit()
