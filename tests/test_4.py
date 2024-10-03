import unittest
from src.FinancePage import FinancePage
from src.test_util import StockTestBase

class StockTest3(StockTestBase):
    # 3. Print all stock symbols in the page data
    def test3(self):
        finance_page = FinancePage(self.driver)
        page_data = finance_page.get_may_be_interested_in_text()

        print("Stock symbols that are in the page data:")
        print(set(page_data))

if __name__ == '__main__':
    unittest.main()