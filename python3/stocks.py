# Raw Package
import numpy as np
from IPython.display import display
import pandas as pd

#Data Source
import yfinance as yf

#Data viz
import plotly.graph_objs as go

from datetime import date
from datetime import timedelta

date1 = date.today()
date2 = date1 - timedelta(days = 1)

today = date1.strftime("%Y-%m-%d")
yesterday = date2.strftime("%Y-%m-%d")


#Interval required 5 minutes
#data = yf.download(tickers='BBIG', period='5d', interval='5m')
#Print data
#print(data)

stocks = ['NVDA', 'GOOG', 'NFLX', 'QQQ', 'F']

data = yf.download(stocks, start=yesterday, end=today)
#print('OPEN\n')
#print(data['Open'])
#print('\nCLOSE')
#print(data['Close'])

df = pd.DataFrame(data)
display(df)

# creating a DataFrame
dict = {'Name' : ['Martha', 'Tim', 'Rob', 'Georgia'],
        'Maths' : [87, 91, 97, 95],
        'Science' : [83, 99, 84, 76]}
df = pd.DataFrame(dict)
 
# displaying the DataFrame
display(df)
