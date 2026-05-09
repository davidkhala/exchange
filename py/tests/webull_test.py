import unittest


class HKTestCase(unittest.TestCase):
    def setUp(self):
        app_key = "d7cda428b1abdd53a2dd558e3d872956"
        app_secret = "bc701f8f53104e9273c3302c4f4f7858"
        from davidkhala.quant.webull.hk import ApiEndpoint, Client
        api_endpoint = ApiEndpoint.Sandbox
        self.client = Client(app_key, app_secret, api_endpoint)

    def test_list(self):
        symbols = self.client.symbols
        self.assertEqual(len(symbols), 16271)
        self.assertIn('00700', [_['symbol'] for _ in symbols])

    def test_history_bar(self):
        print(self.client.history_bar("00700"))

    def test_quote(self):
        print(self.client.quote('00700'))


if __name__ == '__main__':
    unittest.main()
