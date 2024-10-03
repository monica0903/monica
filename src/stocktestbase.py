from selenium import webdriver
import unittest

class StockTestBase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.given_data = ["NFLX", "MSFT", "TSLA"]
        print("Given data:")
        print(self.given_data)

    def tearDown(self):
        self.driver.quit()
