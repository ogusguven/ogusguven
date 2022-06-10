from urllib.request import urlopen
import csv
import numpy as np

# link = "https://api.binance.com/api/v1/ticker/price?symbol=ETHUSDT"
# f = urlopen(link)
# myfile = f.read()
# print(myfile)

ETHDataReread = genfromtxt('binance12hETH.csv', delimiter=',')
BTCDataReread = genfromtxt('binance12hBTC.csv', delimiter=',')


np.savetxt('binance12hETH.csv',[ETHTime12h,ETHValue12h],delimiter=',')
np.savetxt('binance12hBTC.csv',[BTCTime12h,BTCValue12h],delimiter=',')
