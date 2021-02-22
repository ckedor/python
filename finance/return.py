import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt


PG = wb.DataReader('PG', data_source='yahoo', start='1995-1-1')
head = PG.head()
tail = PG.tail()

#simple_return
#(p1 - P0)/P0 = P1/PO - 1

PG['simple_return'] = (PG['Adj Close'] / PG['Adj Close'].shift(1)) - 1
print (PG['simple_return'])

PG['simple_return'].plot(figsize=(8,5))

avg_returns_d = PG['simple_return'].mean()
avg_returns_a = PG['simple_return'].mean()*250

print ( str(round(avg_returns_a, 5) * 100) + " %")


#log return

PG['log_return'] = np.log(PG['Adj Close'] / PG['Adj Close'].shift(1))
print (PG['log_return'])

PG['log_return'].plot(figsize=(8,5))

avg_returns_d = PG['log_return'].mean()
avg_returns_a = PG['log_return'].mean()*250

print ( str(round(avg_returns_a, 5) * 100) + " %")