from enum import Enum

from davidkhala.quant.webull import BaseClient, Category


class ApiEndpoint(str, Enum):
    Production = "api.webull.hk"
    Sandbox = "api.sandbox.webull.hk"


class Client(BaseClient):
    def __init__(self, app_key: str, app_secret: str, api_endpoint: ApiEndpoint):
        super().__init__(app_key, app_secret, api_endpoint, 'hk')

    def quote(self, stock: str, **kwargs):
        return super().quote(stock, category=Category.HK_STOCK)
    def history_bar(self, stock: str, **kwargs):
        return super().history_bar(stock, category=Category.HK_STOCK, **kwargs)
    @property
    def symbols(self):
        return super().symbols(category=Category.HK_STOCK)

