import yfinance as yf
import pandas as pd

from .config import *


class StockData:
    def __init__(self, stock: str):
        self.stock = stock
        self.ticker = yf.Ticker(stock)
        self.data = None
        self.yesterday_close = None
        self.day_before_yesterday_close = None

        self.__get_data()
        '''
        # today's opening price
        self.percent_change = f"{self.stock}: {'🔺' if self.change > 0 else '🔻'}{abs(self.change)}%"
        print(self.close, self.open, self.change, self.percent_change)
        self.news = []
        '''

    def __get_data(self) -> pd.DataFrame:
        self.data = self.ticker.history(period='2d')

        self.difference_close = abs(self.data.loc[YESTERDAY]['Close'] - self.data.loc[DAY_BEFORE_YESTERDAY]['Close'])
        self.difference_gap = (self.difference_close / self.data.loc[YESTERDAY]['Close']) * 100

        return self.data

    def get_news(self):
        return self.ticker.news
