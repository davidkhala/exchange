import logging
from enum import Enum

from davidkhala.utils.http_request import default_on_response
from webull.core.client import ApiClient
from webull.data.common.category import Category
from webull.data.common.timespan import Timespan
from webull.data.data_client import DataClient


class SymbolStatus(str, Enum):
    OpenForClose = 'OC'  # Tradable
    CloseOnly = 'CO'  # Liquidate Only
    NonTradable = 'NT'


class BaseClient:
    def __init__(self, app_key: str, app_secret: str, api_endpoint: str, region_id: str):
        api_client = ApiClient(app_key, app_secret, region_id)
        api_client.add_endpoint(region_id, api_endpoint)
        api_client.set_stream_logger(logging.WARN)
        self.client = DataClient(api_client)
        self.category: Category

    def history_bar(self, stock: str, *, category: Category, timespan: Timespan = Timespan.M1):
        res = self.client.market_data.get_history_bar(stock, category.name, timespan.name)
        return default_on_response(res)

    def quote(self, stock: str, *, category: Category):
        res = self.client.market_data.get_quotes(stock, category.name)
        d = default_on_response(res)

    def paginate_symbols(self, *,
                         category: Category, page: str | None,
                         status: SymbolStatus = SymbolStatus.OpenForClose, size=1000):
        res = self.client.instrument.get_instrument(category=category, status=status.value, last_instrument_id=page,
                                                    page_size=size)
        r = default_on_response(res)
        return r, r[-1]['instrument_id']

    def symbols(self, *, category: Category, size=1000):
        current_page_size = None
        last_id = None
        results = []
        while current_page_size is None or current_page_size == 1000:
            r, last_id = self.paginate_symbols(category=category, page=last_id, size=size)
            results.extend(r)
            current_page_size = len(r)
        return results
