import yfinance as yf
import pandas as pd

from .config import *


class StockData:
    def __init__(self, ticker):
        self.stock = ticker
        self.data = None
        self.yesterday_close = None
        self.day_before_yesterday_close = None

        self.__get_data(ticker)
        '''
        # today's opening price
        self.percent_change = f"{self.stock}: {'🔺' if self.change > 0 else '🔻'}{abs(self.change)}%"
        print(self.close, self.open, self.change, self.percent_change)
        self.news = []
        '''

    def __get_data(self, ticker: str) -> None:
        self.data = yf.download(ticker, start=DAY_BEFORE_YESTERDAY)

        self.yesterday_close = self.data.loc[YESTERDAY]['Adj Close'] if self.data.loc[YESTERDAY]['Adj Close'] else \
            self.data.loc[YESTERDAY]['Close']
        self.day_before_yesterday_close = self.data.loc[DAY_BEFORE_YESTERDAY]['Adj Close'] if \
            self.data.loc[DAY_BEFORE_YESTERDAY]['Adj Close'] else self.data.loc[DAY_BEFORE_YESTERDAY]['Close']

        self.__difference_between_close_prices()
        self.__difference_percentage_close_price()

        return self.data

    def __difference_between_close_prices(self):
        self.difference_close = abs(self.yesterday_close - self.day_before_yesterday_close)
        return self.difference_close

    def __difference_percentage_close_price(self):
        self.close_gap =(self.difference_close / self.yesterday_close) * 100
        return self.close_gap
