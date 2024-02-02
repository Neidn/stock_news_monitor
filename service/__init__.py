from .stock_data import StockData
from .config import *

test_stock = 'AAPL'
stock_data = StockData(test_stock)

if stock_data.difference_gap > THRESHOLD:
    print('Get news')
    print(stock_data.get_news())
