from datetime import datetime
from iexfinance.stocks import get_historical_data
import pandas as pd
### maybe replace hist() with hist(start, end, etc) so you can more easily change important variables



def hist(output=None):
    #if output=='pandas'

    histories = {}
    stock_list = ['AAPL','GOOG','MSFT','AMZN','FB','BABA','JNJ','JPM','XOM']
    names = [x.lower() for x in stock_list]
    start = datetime(2018, 1, 1)
    end = datetime(2019, 1, 1)

    for i in range(len(stock_list)):
        histories[names[i]] = get_historical_data(stock_list[i],start,end,output_format='pandas')
        #output_format='pandas'
    return histories
