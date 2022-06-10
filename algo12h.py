from numpy import genfromtxt
import numpy as np
import matplotlib.pyplot as plt
import functionBank
import rereadData
# BTCTime = h12Freq.BTCTime12h
# BTCValue = h12Freq.BTCValue12h
# ETHTime = h12Freq.ETHTime12h
# ETHValue = h12Freq.ETHValue12h

BTCTime = rereadData.BTCTime12h
BTCValue = rereadData.BTCValue12h
ETHTime = rereadData.ETHTime12h
ETHValue = rereadData.ETHValue12h

##NANINTERPOLATIONS
BTCValue = functionBank.nanInterpolate(BTCValue)
ETHValue = functionBank. nanInterpolate(ETHValue)
## From this point on - 0 is the start day and end is the ending day.
print(BTCValue)
print(ETHValue)
print(ETHTime)
movingAverageDays=2
BTCETHRatioHistorical = functionBank.ratio(BTCValue, ETHValue)
corrx = np.corrcoef(BTCValue, ETHValue)
BTCMovingAv = functionBank.backwards_moving_average(BTCValue,movingAverageDays)
BTCMovingAvDifference = (BTCValue-BTCMovingAv)/BTCMovingAv*100
ETHMovingAv = functionBank.backwards_moving_average(ETHValue,movingAverageDays)
ETHMovingAvDifference = (ETHValue - ETHMovingAv)/ETHMovingAv*100

BTCPercentHistory = functionBank.percent_history(BTCValue)
ETHPercentHistory = functionBank.percent_history(ETHValue)
plt.figure(1)
plt.plot(BTCTime,BTCValue,ETHTime,ETHValue*40)
plt.legend(['BTC Value', 'ETH Value'])
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
# #
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
plt.show(block=False)
#Advance Time

# BTCInit = 500
# # ETHInit = 500
# # fee = 0.001
# # ETHHistory = []
# # BTCHistory = []
# # ETHNumber = []
# # BTCNumber = []
# #
# # ETHMoving = ETHInit
# # BTCMoving = BTCInit
# # ratio = 1 # The ratio of converted amount if a swap is done. Use it to keep distributed assets. 1 is not good.
# # for i in range (0,len(ETHTime)):
# #     ETHHoldValue = ETHMoving+ETHMoving*ETHPercentHistory[i]/100 ### Value of ETH Hold
# #     ETHMoving= ETHHoldValue
# #     ETHHold = ETHMoving/ETHValue[i]                             ### Number of ETH
# #     BTCHoldValue = BTCMoving+BTCMoving*BTCPercentHistory[i]/100    ### Value of BTC Hold
# #     BTCMoving = BTCHoldValue
# #     BTCHold = BTCMoving/BTCValue[i]                             ### Number of BTC
# #     if BTCMovingAvDifference[i]>ETHMovingAvDifference[i]:
# #         ETHMoving,BTCMoving=functionBank.convert_coin(ETHMoving,BTCMoving,ratio,fee)
# #     if ETHMovingAvDifference[i]>BTCMovingAvDifference[i]:
# #         BTCMoving,ETHMoving = functionBank.convert_coin(BTCMoving,ETHMoving,ratio,fee)
# #
# #     ETHHistory.append(ETHHoldValue)
# #     BTCHistory.append(BTCHoldValue)
# # print("ETH:",ETHMoving)
# # print("BTC:",BTCMoving)
# # # for i in range (0,len(ETHTime)):
# # #     if (BTCMovingAvDifference[i]>ETHMovingAvDifference[i] and BTCMovingAvDifference[i]>0):
# # #         ETHMoving,BTCMoving=functionBank.convert_coin(ETHMoving,BTCMoving,ratio,fee)
# # #     if (ETHMovingAvDifference[i]>BTCMovingAvDifference[i] and ETHMovingAvDifference[i]>0):
# # #         BTCMoving,ETHMoving = functionBank.convert_coin(BTCMoving,ETHMoving,ratio,fee)
# # #     if (BTCMovingAvDifference[i]>ETHMovingAvDifference[i] and BTCMovingAvDifference[i]<0):
# # #         ETHMoving,BTCMoving=functionBank.convert_coin(BTCMoving,ETHMoving,ratio,fee)
# # #     if (ETHMovingAvDifference[i]>BTCMovingAvDifference[i] and ETHMovingAvDifference[i]<0):
# # #         BTCMoving,ETHMoving = functionBank.convert_coin(ETHMoving,BTCMoving,ratio,fee)
# # #
# # #     ETHHoldValue = ETHMoving+ETHMoving*ETHPercentHistory[i]/100 ### Value of ETH Hold
# # #     ETHMoving= ETHHoldValue
# # #     ETHHold = ETHMoving/ETHValue[i]                             ### Number of ETH
# # #     BTCHoldValue = BTCMoving+BTCMoving*BTCPercentHistory[i]/100    ### Value of BTC Hold
# # #     BTCMoving = BTCHoldValue
# # #     BTCHold = BTCMoving/BTCValue[i]                             ### Number of BTC
# # #     ETHHistory.append(ETHHoldValue)
# # #     BTCHistory.append(BTCHoldValue)
# #
# # BTCHistory = np.array(BTCHistory)
# # ETHHistory = np.array(ETHHistory)
# # totalValue = BTCHistory+ETHHistory
# # plt.figure(5)
# # plt.plot(ETHTime,ETHHistory,BTCTime,BTCHistory,ETHTime,totalValue)
# # plt.legend(['ETH Wallet','BTC Wallet','Total Value'])
# # plt.grid()
# # plt.show()
# # # plt.figure(6)
# # # plt.plot(ETHTime,totalValue)
# # # plt.legend(['Total Value Algo'])
# # # plt.grid()
# # # plt.show()

print(len(BTC))
startDay = 23
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

plt.figure(2)
plt.plot(BTCTime,BTCValue,BTCTime,BTCVolumeBTCMovingAvDiff+BTCValue,ETHTime,ETHValue+12000,ETHTime,ETHVolumeETHMovingAvDiff+ETHValue+12000)
plt.legend(['BTC','BTCVolumeBTCMovingAvDiff*BTCValue','ETH','ETHVolumeETHMovingAvDiff*ETHValue'])
plt.grid(b=True, which='major')
plt.minorticks_on()
plt.grid(b=True, which='minor', linestyle='--')
plt.show(block=False)
#
# plt.figure(4)
# plt.plot(BTCTime,BTCValue,BTCTime,BTCVolumeBTCMovingAvDiff+BTCValue)
# plt.legend(['BTC','BTCVolumeBTCMovingAvDiff*BTCValue'])
# plt.grid(b=True, which='major')
# plt.minorticks_on()
# plt.grid(b=True, which='minor', linestyle='--')
# plt.show(block=False)

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
# plt.figure(7)
# plt.plot(BTCTime,BTCMovingAvDifference,'bo--',ETHTime,ETHMovingAvDifference,'r*-')
# plt.legend(['BTC Deviation','ETH Deviation'])
# plt.grid()
# plt.show(block=False)
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
# plt.figure(3)
# plt.plot(ETHTime,ETHWalletStat,BTCTime,BTCWalletStat,BTCTime,ETHWalletStat+BTCWalletStat)
# plt.legend(['ETH Wallet','BTC Wallet','Total'])
# plt.grid()
# plt.show(block=False)
#Advance Time

##############################################
###Moving Averages#####
##############################################
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

##############################################
##############################################
##############################################
######################################################################

##Market DIRECTION
#########################
markets_down_criterion = 4
markets_up_criterion = 2
markets_down_history=[]

# ## MOVING AVERAGE BASED
## For Conservative
# for i in range(0,len(ETHTime)):
#     if BTCMovingAvDifference2[i]<-markets_down_criterion or BTCMovingAvDifference2[i]<-markets_down_criterion:
#         markets_down = True
#     if BTCMovingAvDifference2[i-1]<0 and BTCMovingAvDifference2[i]<0:
#         markets_down = True
#     if BTCMovingAvDifference2[i]>markets_up_criterion or BTCMovingAvDifference2[i]>markets_up_criterion:
#         markets_down = False
#     if BTCMovingAvDifference2[i-1]>0 and BTCMovingAvDifference2[i]>0:
#         markets_down = False
#     markets_down_history.append(markets_down)
# markets_down_history= np.array(markets_down_history)

# For very fast increase
for i in range(0,len(ETHTime)):
    if BTCMovingAvDifference2[i]<-markets_down_criterion or BTCMovingAvDifference2[i]<-markets_down_criterion:
        markets_down = True
    if BTCMovingAvDifference2[i-2]<0 and BTCMovingAvDifference2[i-1]<0 and BTCMovingAvDifference2[i]<0:
        markets_down = True
    if BTCMovingAvDifference2[i]>markets_up_criterion or BTCMovingAvDifference2[i]>markets_up_criterion:
        markets_down = False
    if BTCMovingAvDifference2[i-2]>0 and BTCMovingAvDifference2[i-1]>0 and BTCMovingAvDifference2[i]>0:
        markets_down = False
    markets_down_history.append(markets_down)
markets_down_history= np.array(markets_down_history)

### PERCENT HISTORY BASED
# for i in range(0,len(ETHTime)):
#     if BTCPercentHistory[i]<-markets_down_criterion or BTCPercentHistory[i]<-markets_down_criterion:
#         markets_down = True
#     if BTCPercentHistory[i-1]<0 and BTCPercentHistory[i]<0:
#         markets_down = True
#     if BTCPercentHistory[i]>markets_up_criterion or BTCPercentHistory[i]>markets_up_criterion:
#         markets_down = False
#     if BTCPercentHistory[i-1]>0 and BTCPercentHistory[i]>0:
#         markets_down = False
#     markets_down_history.append(markets_down)
# markets_down_history = np.array(markets_down_history)

plt.figure(1)
plt.plot(ETHTime,ETHMovingAvDifference2,'*-',BTCTime,BTCMovingAvDifference2,'o--',BTCTime,markets_down_history,'s')
plt.legend(['ETH Deviation MA2','BTC Deviation MA2'])
plt.grid()
plt.show(block=False)

#######################
#######################


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
EURHoldValue = EURInit
ratio = 1 # The ratio of converted amount if a swap is done. Use it to keep distributed assets. 1 is not good.
for i in range (0,len(ETHTime)):
    ETHHoldValue = ETHMoving+ETHMoving*ETHPercentHistory[i]/100 ### Value of ETH Hold
    ETHMoving= ETHHoldValue
    ETHHold = ETHMoving/ETHValue[i]                             ### Number of ETH
    BTCHoldValue = BTCMoving+BTCMoving*BTCPercentHistory[i]/100    ### Value of BTC Hold
    BTCMoving = BTCHoldValue
    BTCHold = BTCMoving/BTCValue[i]                             ### Number of BTC
    ETHHistory.append(ETHHoldValue)
    BTCHistory.append(BTCHoldValue)
    EURHistory.append(EURHoldValue)
    print('EUR:',EURHoldValue)
    if markets_down_history[i] == 1 and keep_still !=1:
        EURHoldValue = ETHHoldValue + BTCHoldValue-fee
        BTCMoving = 0
        ETHMoving = 0
        keep_still = 1
    if markets_down_history[i] == 0:
        if EURHoldValue != 0:
            BTCMoving = EURHoldValue
            EURHoldValue = 0
        if BTCVolumeBTCMovingAvDiff[i]>ETHVolumeETHMovingAvDiff[i]:
            ETHMoving,BTCMoving=functionBank.convert_coin(ETHMoving,BTCMoving,ratio,fee)
        if ETHVolumeETHMovingAvDiff[i]>BTCVolumeBTCMovingAvDiff[i]:
            BTCMoving,ETHMoving = functionBank.convert_coin(BTCMoving,ETHMoving,ratio,fee)
        keep_still =0
    print('Keep still?:',keep_still)
print("ETH:",ETHMoving)
print("BTC:",BTCMoving)
print("EUR:",EURHoldValue)
BTCHistory = np.array(BTCHistory)
ETHHistory = np.array(ETHHistory)
EURHistory = np.array(EURHistory)
totalValue = BTCHistory+ETHHistory+EURHistory
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