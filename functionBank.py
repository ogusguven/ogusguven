from numpy import genfromtxt
import numpy as np
import matplotlib.pyplot as plt

def dataReader(file, t=','):
    data = genfromtxt(file, delimiter=t,skip_header=2)
    data = np.transpose(data)
    data[0] = (data[0] - data[0][1]) / (data[0][1] - data[0][2])
    return data

def ratio(a, b):
    rat = a / b
    return rat

def nan_helper(y):  ### Helper for Nan helper\n",
    return np.isnan(y), lambda z: z.nonzero()[0]
def nanInterpolate(array1):  ## Function to interpolate NaN values. The array is 1D \n",
    nans, x = nan_helper(array1)
    array1[nans] = np.interp(x(nans), x(~nans), array1[~nans])
    return array1

def moving_average(a, n=3) :
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n
def backwards_moving_average(a, n=3) : #Series, MA Time
    mover = []
    mover[0:n] = np.zeros(n-1)
    for i in range (n-1,len(a)):
        dum = np.cumsum(a[(i-n+1):i+1],dtype=float)
        dumav = dum[n-1]/n
        mover.append(dumav)
    mover = np.array(mover)
    return(mover)
def percent_history(a):
    perc = []
    perc.append(0)
    for i in range(0,len(a)-1):
        dummy =(a[i+1]-a[i])/a[i]
        perc.append(dummy)
    perc = np.array(perc)
    return(perc*100)
def make_data_nice(array, endDay, startDay): ##Start and end day are n days before today startDay>endDay
    array = np.flip(array[endDay:startDay])
    return array

def calculate_value(money,theDay):
    money = money*ETHPercentHistory[theDay]/100+money
    return money

def buy_coin(capital, value):
    amountCoin = capital/value
    return amountCoin, value
def convert_coin(soldAsset,boughtAsset,ratio=1,fee=0):       # Asset1: Asset to sell, Asset 2: Asset to buy, ratio: the ratio of the SOLD amount. Fee: Fee in ratio
    boughtAssetNew = boughtAsset+ratio*soldAsset-fee*soldAsset
    soldAssetNew = soldAsset-ratio*soldAsset
    return soldAssetNew,boughtAssetNew
def largest(num1, num2, num3):
    if (num1 > num2) and (num1 > num3):
        largest_num = num1
    elif (num2 > num1) and (num2 > num3):
        largest_num = num2
    else:
        largest_num = num3
    return largest_num
def smallest(num1, num2, num3):
    if (num1 < num2) and (num1 < num3):
        smallest_num = num1
    elif (num2 < num1) and (num2 < num3):
        smallest_num = num2
    else:
        smallest_num = num3
    return smallest_num