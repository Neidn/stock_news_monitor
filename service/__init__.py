from .stock_data import StockData, make_news_article
from .config import *

test_stock = 'AAPL'
stock_data = StockData(test_stock)

if stock_data.difference_gap < THRESHOLD:
    exit()

news_list = stock_data.get_news()
for news in news_list:
    news_article = make_news_article(news)
    print(news_article)
