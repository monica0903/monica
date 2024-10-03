import unittest
from src.FinancePage import FinancePage
from src.test_util import StockTestBase

class StockTest1(StockTestBase):
    def test1(self):
        finance_page = FinancePage(self.driver)
        assert finance_page.title.__contains__("Google Finance")

if __name__ == '__main__':
    unittest.main()