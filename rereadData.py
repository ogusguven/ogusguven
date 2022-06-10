from numpy import genfromtxt
import numpy as np
import matplotlib.pyplot as plt
import functionBank
import csv

### The 0 of these files is 2020-11-11 08-AM CET
ETHDataReread = genfromtxt('binance12hETH.csv', delimiter=',')
BTCDataReread = genfromtxt('binance12hBTC.csv', delimiter=',')
ETHTime12h = ETHDataReread[0]
ETHValue12h = ETHDataReread[1]
BTCTime12h = BTCDataReread[0]
BTCValue12h = BTCDataReread[1]

print(ETHValue12h)
print(ETHTime12h)
print(BTCValue12h)