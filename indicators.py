#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 14:39:58 2022

@author: tylerpruitt
"""

from objects import Metric

def movingAverage(stockDataList, period):
    """
    Moving Average
    
    Parameters
        stockDataList : a list of StockData objects ordered in time
        period : int, number of closing prices to average for each moving average
    
    Returns
        MA : a list of Metrics with values of moving averages
    """
    
    MA = []
    
    for i in range(len(stockDataList) - period + 1):
        total = 0
        
        for j in range(i, i+period):
            
            total += stockDataList[j].close
        
        total /= period
        
        MA.append(Metric(stockDataList[i + period - 1].datetime, total))
    
    return MA

def exponentialMovingAverage(stockDataList, period, smoothing):
    """
    Weighted Average
    
    Parameters
        stockDataList : a list of StockData objects ordered in time
        period : int, number of closing prices to average for each moving average
        smoothing : float or int, a customizable parameter
    
    Returns
        EMA : a list of Metrics with values of exponential moving averages
    """
    
    EMA = []
    
    # First calculate the moving average for the first length
    MA = 0
    
    for i in range(period):
        MA += stockDataList[i].close
    
    MA /= period
    
    
    EMA.append(Metric(stockDataList[period-1].datetime, MA))
    
    # Calculate the EMA for the rest of the lengths
    for i in range(period, len(stockDataList)):
        EMA.append(Metric(stockDataList[i].datetime, (stockDataList[i].close * (smoothing / (1 + period))) + (EMA[-1] * (1 - (smoothing / (1 + period))))))
    
    return EMA

def relativeStrengthIndex(stockDataList, period):
    """
    Relative Strength Index (RSI)
    
    Parameters
        stockDataList : a list of StockData objects ordered in time
        period : int, number of prices to average for each RSI
    
    Returns
        RSI : a list of Metrics with values of relative strength index
    """
    
    RSI = []
    
    for i in range(len(stockDataList) - period + 1):
        averageGain, averageLoss = 0, 0
        countGain, countLoss = 0, 0
        
        for j in range(i, i+period):
            if stockDataList[j].percentChange > 0:
                countGain += 1
                averageGain += stockDataList[j].percentChange
            elif stockDataList[j].percentChange < 0:
                countLoss += 1
                averageLoss += abs(stockDataList[j].percentChange)
        
        averageGain /= countGain
        averageLoss /= countLoss
        
        RSI.append(Metric(stockDataList[i + period - 1].datetime, 100 - 100 / (1 + (averageGain / averageLoss))))
    
    return RSI

def MACD(stockDataList, fastPeriod, slowPeriod):
    """
    Parameters
    ----------
    stockDataList : a list of StockData objects ordered in time
    fastPeriod : int, a period of data points
    slowPeriod : int, a period of data points

    Returns
    -------
    macd :
    
    Assumes smoothing of 1 in EMA calculation
    """
    macd = []
    
    fastEMA = exponentialMovingAverage(stockDataList, fastPeriod, 1)
    
    slowEMA = exponentialMovingAverage(stockDataList, slowPeriod, 1)
    
    for i in range(len(slowEMA)):
        for j in range(len(fastEMA)):
            if slowEMA[i].datetime == fastEMA[j].datetime:
                macd.append(Metric(slowEMA[i].datetime, fastEMA[j].value - slowEMA[i].value))
    
    return macd
