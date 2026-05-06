import unittest
from davidkhala.quant.itick import Client

class ItickTestCase(unittest.TestCase):
    def setUp(self):
        token = 'eb882d2c0c324999b628a0123d6076cdf9365313ab41435e801d39a66eb0bb47'  # free
        self.client = Client(token)
    def test_stock_quote(self):
        print(self.client.stock_quote('US', 'AAPL'))
        print(self.client.stock_quote('hk', '700'))
    def test_stock_tick(self):
        print(self.client.stock_tick('hk', '700'))




if __name__ == '__main__':
    unittest.main()
