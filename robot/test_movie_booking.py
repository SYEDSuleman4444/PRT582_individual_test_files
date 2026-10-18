
"""
Functional test starter for the Online Movie Booking System.

Check the actual page HTML and update selectors before running.
Requires the application to be running locally.
"""

import os
import unittest
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = os.getenv("BASE_URL", "http://127.0.0.1:8000")
RESULTS_DIR = Path("results/selenium")

# These selectors must match the real application.
SEARCH_INPUT = (By.NAME, "q")
SEARCH_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')


class MovieBookingTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        RESULTS_DIR.mkdir(parents=True, exist_ok=True)
        cls.driver = webdriver.Chrome()
        cls.driver.set_window_size(1366, 900)
        cls.wait = WebDriverWait(cls.driver, 10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.get(BASE_URL)

    def test_01_home_page_loads(self):
        self.assertTrue(
            self.driver.title.strip(),
            "The home page should have a title"
        )

    def test_02_search_existing_movie(self):
        search = self.wait.until(
            EC.visibility_of_element_located(SEARCH_INPUT)
        )
        search.clear()
        search.send_keys("Venom")
        self.driver.find_element(*SEARCH_BUTTON).click()

        self.wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        self.assertIn("venom", self.driver.page_source.lower())

    def test_03_search_nonexistent_movie(self):
        search = self.wait.until(
            EC.visibility_of_element_located(SEARCH_INPUT)
        )
        search.clear()
        search.send_keys("Nonexistent123XYZ")
        self.driver.find_element(*SEARCH_BUTTON).click()

        body = self.wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        text = body.text.lower()

        expected_messages = [
            "no items found",
            "no movies found",
            "no results"
        ]
        self.assertTrue(
            any(message in text for message in expected_messages),
            "A clear no-results message should be displayed"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
