#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 14:39:58 2022

@author: tylerpruitt
"""

"""
Still need to implement MACD and RSI (Relative Strength Index)
"""

def movingAverage(closingPrices, period, datetimes=[]):
    """
    Moving Average
    
    Parameters:
        closingPrices: a list of closing prices
        period: int, number of closing prices to average for each moving average
        datetimes: optional, a list of strings of datetimes corresponding to the closing prices
    
    Returns:
        MA: a list of moving averages
        times: a list of strings of datetimes corresponding to the moving averages
    """
    
    MA, times = [], []
    
    for i in range(len(closingPrices) - period+1):
        total = 0
        
        for j in range(i, i+period):
            
            total += closingPrices[j]
        
        total /= period
        
        if datetimes != []:
            times.append(datetimes[i+period-1])
        
        MA.append(total)
    
    return MA, times

def exponentialMovingAverage(closingPrices, period, smoothing, datetimes=[]):
    """
    Weighted Average
    
    Parameters:
        closingPrices: a list of closing prices
        period: int, number of closing prices to average for each moving average
        smoothing: float or int, a customizable parameter
        datetimes: optional, a list of strings of datetimes corresponding to the closing prices
    
    Returns:
        EMA: a list of exponential moving averages
        times: a list of strings of datetimes corresponding to the exponential moving averages
    """
    
    EMA, times = [], []
    
    # First calculate the moving average for the first length
    MA = 0
    
    for i in range(period):
        MA += closingPrices[i]
    
    MA /= period
    
    if datetimes != []:
        times.append(datetimes[period-1])
    
    EMA.append(MA)
    
    # Calculate the EMA for the rest of the lengths
    for i in range(period, len(closingPrices)):
        
        EMA.append((closingPrices[i] * (smoothing / (1 + period))) + (EMA[-1] * (1 - (smoothing / (1 + period)))))
        
        if datetimes != []:
            times.append(datetimes[i])
    
    return EMA, times
