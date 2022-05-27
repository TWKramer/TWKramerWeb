import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
plt.style.use('seaborn')

import yfinance as yf


""" style.use ('ggplot')
start = dt.datetime(2010,1,1)
end = dt.datetime(2016,12,31)

df = web.DataReader('TSLA', 'yahoo', start, end)
print(df.tail()) #code automatically shows 5 results
#print(df.head(10))       code automatically shows 10 results
#print(df.tail())          code automatically shows the last results... hence head and tail """

msft = yf.Ticker('msft')

""" print(type(msft.info)) """

stockinfo = msft.info 

""" for key,value in stockinfo.items():
    print(key, ":", value)

print(msft.dividends)
print(msft.institutional_holders)

df = msft.dividends

data = df.resample('Y').sum()

data = data.reset_index()

data['Year'] = data['Date'].dt.year

plt.figure()
plt.bar(data['Year'], data['Dividends'])
plt.ylabel('Dividend Yield ($)')
plt.xlabel('Year')
plt.title ('Microsoft Dividend History')
plt.xlim(2002, 2020)
plt.show() """


""" df = msft.history(period='max')

plt.figure()
plt.plot(df['Close'])
plt.show()
 """


print(msft.dividends)