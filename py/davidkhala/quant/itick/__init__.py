from itick.sdk import Client as RawClient

RawClient.BASE_URL = "https://api0.itick.org"
class Client:

    def __init__(self, api_token: str):
        self.client = RawClient(api_token)

    def stock_quote(self, region: str, code: str):

        return self.client.get_stock_quote(region, code)
    def stock_tick(self, region: str, code: str):
        return self.client.get_stock_tick(region, code)
    def stock_line(self, region: str, code: str, period, limit):
        return self.client.get_stock_kline(region, code, period, limit)