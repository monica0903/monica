import unittest
from src.FinancePage import FinancePage
from src.stocktestbase import StockTestBase

class StockTest5(StockTestBase):
    # 5. Print all stock symbols that are in the page data but not in the given data
    def test5(self):
        finance_page = FinancePage(self.driver)
        page_data = finance_page.get_may_be_interested_in_text()
        print("Page data:")
        print(page_data)

        print("Stock symbols that are in the page data but not in the given data:")
        print(set(page_data) - set(self.given_data))

if __name__ == '__main__':
    unittest.main()