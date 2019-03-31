from iexfinance import get_historical_data
from datetime import datetime
import pandas as pd
import talib as ta
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('bmh')

start = datetime(2018,1,1)
end = datetime(2019,1,1)

data = get_historical_data('AAPL', start=start, end=end, output_format='pandas')
data.index = pd.to_datetime(data.index)
data.head()

data['SMA'] = ta.SMA(data.close, timeperiod = 20)
data['EMA'] = ta.EMA(data.close, timeperiod = 20)

data[['close', 'SMA', 'EMA']].plot(figsize=(10,5))
plt.show()
