import tushare as ts
import talib
from matplotlib import pyplot as plt

df=ts.get_k_data('601888',start='2018-01-30',end='2018-10-30') 
closed=df['close'].values
ma5=talib.SMA(closed,timeperiod=5)
ma10=talib.SMA(closed,timeperiod=10)
ma20=talib.SMA(closed,timeperiod=20)

print (closed)
print (ma5)
print (ma10)
print (ma20)

plt.plot(closed)
plt.plot(ma5)
plt.plot(ma10)
plt.plot(ma20)
plt.grid()
plt.show()

