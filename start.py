from datetime import datetime
from iexfinance.stocks import Stock, get_historical_data



#aapl = Stock('AAPL')
#print(aapl.get_price())


start = datetime(2019, 3, 1)

aapl_hist = get_historical_data('AAPL',start,end=None)
goog_hist = get_historical_data('GOOG',start,end=None,output_format='pandas')
msft_hist = get_historical_data('MSFT',start,end=None,output_format='pandas')
amzn_hist = get_historical_data('AMZN',start,end=None,output_format='pandas')
fb_hist   = get_historical_data('FB',start,end=None,output_format='pandas')
baba_hist = get_historical_data('BABA',start,end=None,output_format='pandas')
jnj_hist  = get_historical_data('JNJ',start,end=None,output_format='pandas')
jpm_hist  = get_historical_data('JPM',start,end=None,output_format='pandas')
xom_hist  = get_historical_data('XOM',start,end=None,output_format='pandas')
bac_hist  = get_historical_data('BAC',start,end=None,output_format='pandas')
wmt_hist  = get_historical_data('WMT',start,end=None,output_format='pandas')
wfc_hist  = get_historical_data('WFC',start,end=None,output_format='pandas')
v_hist    = get_historical_data('V',start,end=None,output_format='pandas')
pg_hist   = get_historical_data('PG',start,end=None,output_format='pandas')
bud_hist  = get_historical_data('BUD',start,end=None,output_format='pandas')

#print(aapl_hist['2019-03-18']['close'])

aapl_close = []
for key,value in aapl_hist.items():
    aapl_close.append(aapl_hist[key]['close'])

print(aapl_close)



#  #  move historical data calls into function, or separate fil e
