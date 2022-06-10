from numpy import genfromtxt
import numpy as np
import matplotlib.pyplot as plt
import functionBank
BTCData = 'Binance_BTCUSDT_d.csv'
ETHData = 'Binance_ETHUSDT_d.csv'


BTC = functionBank.dataReader(BTCData)
ETH = functionBank.dataReader(ETHData)

print(len(BTC))
startDay = 300
endDay = 0
BTCTime = functionBank.make_data_nice(BTC[0],endDay,startDay)
BTCValue = functionBank.make_data_nice(BTC[3],endDay,startDay) ## 3 is close value of a day
BTCVolumeBTC = functionBank.make_data_nice(BTC[7],endDay,startDay)
BTCVolumeUSD = functionBank.make_data_nice(BTC[8],endDay,startDay)
ETHVolumeETH = functionBank.make_data_nice(ETH[7],endDay,startDay)
ETHVolumeUSD = functionBank.make_data_nice(ETH[8],endDay,startDay)

ETHTime = functionBank.make_data_nice(ETH[0],endDay,startDay)
ETHValue = functionBank.make_data_nice(ETH[3],endDay,startDay) ## 3 is close value of a day
##NANINTERPOLATIONS
BTCValue = functionBank.nanInterpolate(BTCValue)
ETHValue = functionBank. nanInterpolate(ETHValue)
## From this point on - 0 is the start day and end is the ending day.
print(BTCValue)
print(ETHValue)
print(ETHTime)
movingAverageDays=5

BTCETHRatioHistorical = functionBank.ratio(BTCValue, ETHValue)
corrx = np.corrcoef(BTCValue, ETHValue)
print(corrx)
BTCMovingAv = functionBank.backwards_moving_average(BTCValue,movingAverageDays)
BTCMovingAvDifference = (BTCValue-BTCMovingAv)/BTCMovingAv*100
ETHMovingAv = functionBank.backwards_moving_average(ETHValue,movingAverageDays)
ETHMovingAvDifference = (ETHValue - ETHMovingAv)/ETHMovingAv*100
BTCVolumeUSDMovingAv = functionBank.backwards_moving_average(BTCVolumeUSD,movingAverageDays)
BTCVolumeUSDMovingAvDiff = (BTCVolumeUSD - BTCVolumeUSDMovingAv)/BTCVolumeUSDMovingAv*100
BTCVolumeBTCMovingAv = functionBank.backwards_moving_average(BTCVolumeBTC,movingAverageDays)
BTCVolumeBTCMovingAvDiff= (BTCVolumeBTC - BTCVolumeBTCMovingAv)/BTCVolumeBTCMovingAv*100
ETHVolumeUSDMovingAv = functionBank.backwards_moving_average(ETHVolumeUSD,movingAverageDays)
ETHVolumeUSDMovingAvDiff = (ETHVolumeUSD - ETHVolumeUSDMovingAv)/ETHVolumeUSDMovingAv*100
ETHVolumeETHMovingAv = functionBank.backwards_moving_average(ETHVolumeETH,movingAverageDays)
ETHVolumeETHMovingAvDiff= (ETHVolumeETH - ETHVolumeETHMovingAv)/ETHVolumeETHMovingAv*100

BTCPercentHistory = functionBank.percent_history(BTCValue)
ETHPercentHistory = functionBank.percent_history(ETHValue)

BTCMovingAv2 = functionBank.backwards_moving_average(BTCValue,2)
BTCMovingAvDifference2 = (BTCValue-BTCMovingAv2)/BTCMovingAv2*100
ETHMovingAv2 = functionBank.backwards_moving_average(ETHValue,2)
ETHMovingAvDifference2 = (ETHValue - ETHMovingAv2)/ETHMovingAv2*100


BTCMovingAv3 = functionBank.backwards_moving_average(BTCValue,3)
BTCMovingAvDifference3 = (BTCValue-BTCMovingAv)/BTCMovingAv*100
ETHMovingAv3 = functionBank.backwards_moving_average(ETHValue,3)
ETHMovingAvDifference3 = (ETHValue - ETHMovingAv)/ETHMovingAv*100

BTCMovingAv5 = functionBank.backwards_moving_average(BTCValue,5)
BTCMovingAvDifference5 = (BTCValue-BTCMovingAv)/BTCMovingAv*100
ETHMovingAv5 = functionBank.backwards_moving_average(ETHValue,5)
ETHMovingAvDifference5 = (ETHValue - ETHMovingAv)/ETHMovingAv*100

BTCMovingAv7 = functionBank.backwards_moving_average(BTCValue,7)
BTCMovingAvDifference7 = (BTCValue-BTCMovingAv)/BTCMovingAv*100
ETHMovingAv7 = functionBank.backwards_moving_average(ETHValue,7)
ETHMovingAvDifference7 = (ETHValue - ETHMovingAv)/ETHMovingAv*100






markets_down_criterion = 4
markets_up_criterion = 4
markets_down_history=[]
for i in range(0,len(ETHTime)):
    if BTCMovingAvDifference[i]<-markets_down_criterion or ETHMovingAvDifference[i]<-markets_down_criterion:
        markets_down = True
    if BTCMovingAvDifference[i-1]<0 and BTCMovingAvDifference[i]<0:
        markets_down = True
    if BTCMovingAvDifference[i]>markets_up_criterion or ETHMovingAvDifference[i]>markets_up_criterion:
        markets_down = False
    if BTCMovingAvDifference[i-1]>0 and BTCMovingAvDifference[i]>0:
        markets_down = False
    markets_down_history.append(markets_down)
markets_down_history = np.array(markets_down_history)

plt.figure(1)
plt.plot(BTCTime,BTCMovingAvDifference,'bo--',ETHTime,ETHMovingAvDifference,'r*-',BTCTime,markets_down_history,'s')
plt.legend(['BTC Deviation','ETH Deviation'])
plt.grid()
plt.show(block=False)


ETHInit = 500
BTCInit = 500

# This block is the scenereo where all money is once invested on an asset - Not an algo but a simulation - Carry this to hypotetical functions

ETHWalletStat = []
ETHWalletStat.append(ETHInit)
ETHAssetDumStat = ETHWalletStat[0]
for i in range(1,len(ETHValue)):
    ETHAssetDumStat = ETHAssetDumStat*ETHPercentHistory[i]/100+ETHAssetDumStat
    ETHWalletStat.append(ETHAssetDumStat)
ETHWalletStat = np.array(ETHWalletStat)

BTCWalletStat = []
print(type(BTCWalletStat))
BTCWalletStat.append(BTCInit)
BTCAssetDumStat = BTCWalletStat[0]
for j in range(1,len(BTCValue)):
    BTCAssetDumStat = BTCAssetDumStat*BTCPercentHistory[j]/100+BTCAssetDumStat
    BTCWalletStat.append(BTCAssetDumStat)
BTCWalletStat = np.array(BTCWalletStat)
print(len(ETHWalletStat))
print(len(BTCWalletStat))
print(len(ETHWalletStat+BTCWalletStat))
plt.figure(3)
plt.plot(ETHTime,ETHWalletStat,BTCTime,BTCWalletStat,BTCTime,ETHWalletStat+BTCWalletStat)
plt.legend(['ETH Wallet','BTC Wallet','Total'])
plt.grid()
plt.show(block=False)


BTCMovingAv3 = functionBank.backwards_moving_average(BTCValue,3)
BTCMovingAvDifference3 = (BTCValue-BTCMovingAv)/BTCMovingAv*100
ETHMovingAv3 = functionBank.backwards_moving_average(ETHValue,3)
ETHMovingAvDifference3 = (ETHValue - ETHMovingAv)/ETHMovingAv*100

BTCMovingAv5 = functionBank.backwards_moving_average(BTCValue,5)
BTCMovingAvDifference5 = (BTCValue-BTCMovingAv)/BTCMovingAv*100
ETHMovingAv5 = functionBank.backwards_moving_average(ETHValue,5)
ETHMovingAvDifference5 = (ETHValue - ETHMovingAv)/ETHMovingAv*100

BTCMovingAv7 = functionBank.backwards_moving_average(BTCValue,7)
BTCMovingAvDifference7 = (BTCValue-BTCMovingAv)/BTCMovingAv*100
ETHMovingAv7 = functionBank.backwards_moving_average(ETHValue,7)
ETHMovingAvDifference7 = (ETHValue - ETHMovingAv)/ETHMovingAv*100

BTCVolumeBTCMovingAv3 = functionBank.backwards_moving_average(BTCVolumeBTC,3)
BTCVolumeBTCMovingAvDiff3= (BTCVolumeBTC - BTCVolumeBTCMovingAv3)/BTCVolumeBTCMovingAv3*100
ETHVolumeETHMovingAv3 = functionBank.backwards_moving_average(ETHVolumeETH,3)
ETHVolumeETHMovingAvDiff3= (ETHVolumeETH - ETHVolumeETHMovingAv3)/ETHVolumeETHMovingAv3*100

BTCVolumeBTCMovingAv5 = functionBank.backwards_moving_average(BTCVolumeBTC,5)
BTCVolumeBTCMovingAvDiff5= (BTCVolumeBTC - BTCVolumeBTCMovingAv5)/BTCVolumeBTCMovingAv3*100
ETHVolumeETHMovingAv5 = functionBank.backwards_moving_average(ETHVolumeETH,5)
ETHVolumeETHMovingAvDiff5= (ETHVolumeETH - ETHVolumeETHMovingAv5)/ETHVolumeETHMovingAv5*100

BTCVolumeBTCMovingAv7 = functionBank.backwards_moving_average(BTCVolumeBTC,7)
BTCVolumeBTCMovingAvDiff7= (BTCVolumeBTC - BTCVolumeBTCMovingAv7)/BTCVolumeBTCMovingAv7*100
ETHVolumeETHMovingAv7 = functionBank.backwards_moving_average(ETHVolumeETH,7)
ETHVolumeETHMovingAvDiff7= (ETHVolumeETH - ETHVolumeETHMovingAv7)/ETHVolumeETHMovingAv7*100

plt.figure(5)
plt.plot(ETHTime,ETHValue,ETHTime,ETHMovingAv3,ETHTime,ETHMovingAv5,ETHTime,ETHMovingAv7)
plt.legend(['ETH Value','ETH Moving Average for 3 days','ETH Moving Average for 5 days','ETH Moving Average for 7 days'])
plt.grid()
plt.show(block=False)
plt.figure(6)
plt.plot(ETHTime,ETHValue,ETHTime,ETHVolumeETHMovingAv3/1500,'*-',ETHTime,ETHVolumeETHMovingAv5/1500,'o-',ETHTime,ETHVolumeETHMovingAv7/1500,'*-')
plt.legend(['ETH Value','ETH Volume ETH Moving Average for 3 days','ETH Volume ETH Moving Average for 5 days','ETH Volume ETH Moving Average for 7 days'])
plt.grid(b=True, which='major')
plt.minorticks_on()
plt.grid(b=True, which='minor', linestyle='--')
plt.show(block=False)
plt.figure(7)
plt.plot(BTCTime,BTCValue,BTCTime,BTCVolumeBTCMovingAv3/5,'*-',BTCTime,BTCVolumeBTCMovingAv5/5,'o-',BTCTime,BTCVolumeBTCMovingAv7/5,'*-')
plt.legend(['BTC Value','BTC Volume BTC Moving Average for 3 days','BTC Volume BTC Moving Average for 5 days','BTC Volume BTC Moving Average for 7 days'])
plt.grid(b=True, which='major')
plt.minorticks_on()
plt.grid(b=True, which='minor', linestyle='--')
plt.show()

