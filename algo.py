from numpy import genfromtxt
import numpy as np
import matplotlib.pyplot as plt
import functionBank


BTCData = 'Binance_BTCUSDT_d.csv'
ETHData = 'Binance_ETHUSDT_d.csv'


BTC = functionBank.dataReader(BTCData)
ETH = functionBank.dataReader(ETHData)

print(len(BTC))
startDay = 1050
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

# plt.figure(1)
# plt.plot(BTCTime,BTCValue,ETHTime,ETHValue*40)
# plt.legend(['BTC Value', 'ETH Value'])
# plt.show(block=False)

plt.figure(1)
plt.plot(BTCTime,BTCValue/ETHValue*500,BTCTime,BTCValue)
plt.legend(['BTC/ETH Value','BTC Value'])
plt.show(block=False)
plt.grid()

plt.figure(2)
plt.plot(BTCTime,BTCValue,BTCTime,BTCVolumeBTCMovingAvDiff+BTCValue)
plt.legend(['BTC','BTCVolumeBTCMovingAvDiff*BTCValue'])
plt.grid(b=True, which='major')
plt.minorticks_on()
plt.grid(b=True, which='minor', linestyle='--')
plt.show(block=False)

plt.figure(4)
plt.plot(BTCTime,BTCValue,BTCTime,BTCVolumeBTCMovingAvDiff+BTCValue)
plt.legend(['BTC','BTCVolumeBTCMovingAvDiff*BTCValue'])
plt.grid(b=True, which='major')
plt.minorticks_on()
plt.grid(b=True, which='minor', linestyle='--')
plt.show(block=False)

# plt.figure(2)
# plt.plot(BTCTime, BTCETHRatioHistorical[0:365])
# plt.show()

# plt.figure(3)
# plt.plot(BTC[0][0:365],np.gradient(BTC[3][0:365],15),ETH[0][0:365],np.gradient(ETH[3][0:365]*40,15))
# plt.legend(['BTC','ETH'])
# plt.show()

#plt.figure(2)
#plt.plot(BTC[0][0:365],BTC[3][0:365],BTC[0][0:365],BTCMovingAv[0:365])
#plt.legend(['BTC','BTC Moving Average'])
#plt.show()

# plt.figure(2)
# plt.plot(BTCTime,BTCValue,BTCTime,BTCMovingAv,ETHTime,ETHValue*40,ETHTime,ETHMovingAv*40)
# plt.legend(['BTC','BTC Moving Average','ETH','ETH Moving Average'])
# plt.show(block=False)
# plt.clf()
#
plt.figure(7)
plt.plot(BTCTime,BTCMovingAvDifference,'bo--',ETHTime,ETHMovingAvDifference,'r*-')
plt.legend(['BTC Deviation','ETH Deviation'])
plt.grid()
plt.show(block=False)
# # #
# plt.figure(4)
# plt.plot(BTCTime,BTCPercentHistory,'bo--',ETHTime,ETHPercentHistory,'r*-')
# plt.legend(['BTC Percent History','ETH Percent History'])
# plt.grid()
# plt.show(block=False)

#plt.figure(3)
#plt.plot(BTC[0][0:365],np.gradient(BTC[3][0:365],15),BTC[0][0:365],np.gradient(BTCMovingAv[0:365],15))
#plt.legend(['BTC Gradient','BTC Moving Average Gradient'])
#plt.show()

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
# plt.show(block=False)
#Advance Time

BTCInit = 1000
ETHInit = 0
EURInit = 0
fee = 0.001
ETHHistory = []
BTCHistory = []
EURHistory = []
ETHNumber = []
BTCNumber = []

ETHMoving = ETHInit
BTCMoving = BTCInit
EURMoving = EURInit
ratio = 1 # The ratio of converted amount if a swap is done. Use it to keep distributed assets. 1 is not good.
for i in range (0,len(ETHTime)):
    ETHHoldValue = ETHMoving+ETHMoving*ETHPercentHistory[i]/100 ### Value of ETH Hold
    ETHMoving= ETHHoldValue
    ETHHold = ETHMoving/ETHValue[i]                             ### Number of ETH
    BTCHoldValue = BTCMoving+BTCMoving*BTCPercentHistory[i]/100    ### Value of BTC Hold
    BTCMoving = BTCHoldValue
    BTCHold = BTCMoving/BTCValue[i]                             ### Number of BTC
    EURHoldValue = EURMoving
    if BTCVolumeBTCMovingAvDiff[i]>ETHVolumeETHMovingAvDiff[i]:
            ETHMoving,BTCMoving=functionBank.convert_coin(ETHMoving,BTCMoving,ratio,fee)
    if ETHVolumeETHMovingAvDiff[i]>BTCVolumeBTCMovingAvDiff[i]:
            BTCMoving,ETHMoving = functionBank.convert_coin(BTCMoving,ETHMoving,ratio,fee)
    ETHHistory.append(ETHHoldValue)
    BTCHistory.append(BTCHoldValue)
    EURHistory.append(EURHoldValue)

print("ETH:",ETHMoving)
print("BTC:",BTCMoving)
print("EUR:",EURMoving)
BTCHistory = np.array(BTCHistory)
ETHHistory = np.array(ETHHistory)
totalValue = BTCHistory+ETHHistory
plt.figure(5)
plt.plot(ETHTime,ETHHistory,BTCTime,BTCHistory,ETHTime,totalValue)
plt.legend(['ETH Wallet','BTC Wallet','Total Value'])
plt.grid()
plt.show()
# plt.figure(6)
# plt.plot(ETHTime,totalValue)
# plt.legend(['Total Value Algo'])
# plt.grid()
# plt.show()