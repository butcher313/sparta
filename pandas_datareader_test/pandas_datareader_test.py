import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt
import pandas as pd

# start = datetime.datetime(2016, 2, 19)
# end = datetime.datetime(2016, 3, 4)

# gs = web.DataReader("078930.KS", "yahoo")

# plt.plot(gs['Adj Close'])

# plt.show()

gs = web.DataReader("078930.KS", "yahoo")


new_gs = gs[gs['Volume'] != 0]

ma5 = new_gs['Adj Close'].rolling(window=5).mean()

new_gs.insert(len(new_gs.columns), "MA5", ma5)

ma20 = new_gs['Adj Close'].rolling(window=20).mean()

ma60 = new_gs['Adj Close'].rolling(window=60).mean()

ma120 = new_gs['Adj Close'].rolling(window=120).mean()

# 이평선 20, 60, 120도 추가
new_gs.insert(len(new_gs.columns), "MA20", ma20)
new_gs.insert(len(new_gs.columns), "MA60", ma60)
new_gs.insert(len(new_gs.columns), "MA120", ma120)


plt.plot(new_gs.index, new_gs['Adj Close'], label='Adj Close')

plt.plot(new_gs.index, new_gs['MA5'], label="MA5")
plt.plot(new_gs.index, new_gs['MA20'], label="MA20")
plt.plot(new_gs.index, new_gs['MA60'], label="MA60")
plt.plot(new_gs.index, new_gs['MA120'], label="MA120")

plt.legend(loc='best')
plt.grid()
plt.show()