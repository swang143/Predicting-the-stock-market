import pandas as pd
import numpy as np
from datetime import datetime

df = pd.read_csv('sphist.csv')
df.Date = pd.to_datetime(df.Date)
df = df.sort('Date', ascending=True)
#print(df.columns.values)

#['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close']

"""
Indicators that I choose:
The average price from the past 5 days
The ratio between the average price for the past 5 days, and the average price for the past 365 days
The standard deviation of the price over the past 5 days
"""
#pd.set_option('display.precision',6)
# Doesn't work in rounding the significant number
# Find out the date of the first day in stock market data The day 365 days after first day is the starting day we can calculate
first_index = df.index.values[0]
print(df.loc[first_index-365]['Date'])

for index, row in df[df['Date'] >= df.loc[first_index-365]['Date']].iterrows():
    row['day_5'] = df.loc[index+5:index+1,'Close'].mean()
    row['day_365'] = df.loc[index+365:index+1, 'Close'].mean()
    row['ratio'] = row['day_5']/row['day_365']
    row['day_5_std'] = np.std(df.loc[index+5:index+1,'Close'])
    # print(row[['day_5','ratio','day_5_std']])

# Data cleaning process for the following
"""
Some of the indicators use 365 days of historical
data, and the dataset starts on 1951-06-19. Thus,
any rows that fall before 1951-06-19 don't have
enough historical data to compute all the
indicators. We'll need to remove these rows before
we split the data.
"""

    
    

