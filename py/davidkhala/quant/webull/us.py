from enum import Enum

from webull.data.common.category import Category

from davidkhala.quant.webull import BaseClient


class ApiEndpoint(str, Enum):
    Test = "us-openapi-alb.uat.webullbroker.com",
    Production = "api.webull.com"


class Client(BaseClient):
    def __init__(self, app_key: str, app_secret: str, api_endpoint: ApiEndpoint):
        super().__init__(app_key, app_secret, api_endpoint, 'us')

    def history_bar(self, stock: str, **kwargs):
        return super().history_bar(stock, category=Category.US_STOCK, **kwargs)
