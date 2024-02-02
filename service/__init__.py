from .stock_data import StockData

stock_data = StockData('AAPL')

print(stock_data.close_gap)

if stock_data.close_gap > 1:
    print('🔺')
