#!/bin/python
import matplotlib.pyplot as plt
import pandas_datareader as pdr
import sys
from datetime import datetime

def graph_data(stock, start, end):
    stock_data = pdr.get_data_google(stock)[start: end]

    date = stock_data['Close'].index
    closep = stock_data['Close'].values

    plt.plot_date(date, closep, '-', label='Price')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.title(stock + ' Stock Price')
    plt.legend()
    plt.show()


start_date = datetime(2007, 8, 25)
end_date = datetime(2017, 8, 25)
stock_name = sys.argv[1]

if stock_name == '--help' or stock_name == '-h':
    print('finance {stock | --help | -h}')
    print('AAPL  :: Apple')
    print('GOOGL :: Google')
    print('TSLA  :: Tesla')
    print('MSFT  :: Microsoft')
    print('HKG   :: Lenovo')
else:
    graph_data(stock_name, start_date, end_date)
