import unittest
from src.FinancePage import FinancePage
from src.stocktestbase import StockTestBase

class StockTest6(StockTestBase):
    # 6. Print all stock symbols that are in the given data but not in the page data
    def test6(self):
        finance_page = FinancePage(self.driver)
        page_data = finance_page.get_may_be_interested_in_text()
        print("Page data:")
        print(page_data)

        print("Stock symbols that are in the given data but not in the page data:")
        print(set(self.given_data) - set(page_data))

if __name__ == '__main__':
    unittest.main()