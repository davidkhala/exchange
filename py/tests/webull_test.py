import unittest
from davidkhala.quant.webull import Client, ApiEndpoint


class HistoryTestCase(unittest.TestCase):
    def setUp(self):
        app_key = ""
        app_secret = ""
        api_endpoint = ApiEndpoint.Test
        self.client = Client(app_key, app_secret, api_endpoint)

    def test_history_bar(self):
        print(self.client.history_bar("AAPL"))


if __name__ == '__main__':
    unittest.main()
