from numpy import genfromtxt
import numpy as np
import matplotlib.pyplot as plt
import functionBank
import csv

BTCData = 'Binance_BTCUSDT_1h.csv'
ETHData = 'Binance_ETHUSDT_1h.csv'
# BTCData = 'Coinbase_BTCUSD_1h.csv'
# ETHData = 'Coinbase_ETHUSD_1h.csv'

def dataReader(file, t=','):
    data = genfromtxt(file, delimiter=t,skip_header=2)
    data = np.transpose(data)
    data[0] = (data[0] - data[0][1]) / (data[0][1] - data[0][2])-1
    return data
BTC = dataReader(BTCData)
ETH = dataReader(ETHData)
print(len(BTC))
BTCTime = BTC[0]
BTCValue = BTC[3]
print(BTC[0][0])
## First dataset is 8AM 11-11-2020 for this case. Update file every 12 hours i.e. every day at 8AM and 8PM

BTCTime12h = []
BTCValue12h = []
ETHTime12h = []
ETHValue12h = []
for i in range(0,len(BTC[0]),12):
    BTCTime12h.append(BTC[0][i])
    BTCValue12h.append(BTC[3][i])
    ETHTime12h.append(ETH[0][i])
    ETHValue12h.append(ETH[3][i])
endofTime = 0
startofTime = 64 ##8 Days
def make_data_nice(array, endDay, startDay): ##Start and end day are n days before today startDay>endDay
    array = np.flip(array[endDay:startDay])
    return array
BTCTime12h = functionBank.make_data_nice(BTCTime12h,endofTime,startofTime)
BTCTime12h = BTCTime12h/12
BTCValue12h = functionBank.make_data_nice(BTCValue12h,endofTime,startofTime)
ETHTime12h = functionBank.make_data_nice(ETHTime12h,endofTime,startofTime)
ETHTime12h = ETHTime12h/12
ETHValue12h = functionBank.make_data_nice(ETHValue12h,endofTime,startofTime)
print(len(BTCTime12h))
print(BTCTime12h)
print(BTCValue12h)
print(ETHTime12h)
print(ETHValue12h)

np.savetxt('binance12hETH.csv',[ETHTime12h,ETHValue12h],delimiter=',')
np.savetxt('binance12hBTC.csv',[BTCTime12h,BTCValue12h],delimiter=',')

