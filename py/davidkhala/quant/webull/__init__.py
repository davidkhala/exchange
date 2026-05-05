from enum import Enum

from webull.data.common.category import Category
from webull.data.common.timespan import Timespan
from webull.core.client import ApiClient
from webull.data.data_client import DataClient
from davidkhala.utils.http_request import default_on_response


class ApiEndpoint(str, Enum):
    Test = "us-openapi-alb.uat.webullbroker.com",
    Production = "api.webull.com"


class Client:
    def __init__(self, app_key: str, app_secret: str, api_endpoint: ApiEndpoint):
        api_client = ApiClient(app_key, app_secret, "us")
        api_client.add_endpoint("us", api_endpoint)
        self.client = DataClient(api_client)

    def history_bar(self, stock: str):
        res = self.client.market_data.get_history_bar(stock, Category.US_STOCK.name, Timespan.M1.name)
        return default_on_response(res)
