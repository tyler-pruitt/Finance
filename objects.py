#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 17:40:38 2022

@author: tylerpruitt
"""

class StockData(object):
    def __init__(self, datetime, openPrice, highPrice, lowPrice, closePrice, adjClose, volume, ticker):
        self.datetime = datetime
        self.year = int(datetime[:4])
        self.month = int(datetime[5:7])
        self.day = int(datetime[8:10])
        
        self.hour = int(datetime[11:13])
        self.minute = int(datetime[14:16])
        self.second = int(datetime[17:19])
        
        self.open = openPrice
        self.high = highPrice
        self.low = lowPrice
        self.close = closePrice
        self.adjClose = adjClose
        self.volume = volume
        self.ticker = ticker
        
        self.percentChange = 100 * (self.close - self.open) / self.open
    
    def __repr__(self):
        return '(' + self.ticker + ', ' + self.datetime + ', %Change: ' + str(self.percentChange) + ', Open: ' + str(self.open) + ', High: ' + str(self.high) + ', Low: ' + str(self.low) + ', Close: ' + str(self.close) + ', Adj.Close: ' + str(self.adjClose) + ', Volume: ' + str(self.volume) + ')'
    
    def __str__(self):
        return '(' + self.ticker + ', ' + self.datetime + ', %Change: ' + str(self.percentChange) + ')'

class Metric(object):
    def __init__(self, datetime, value):
        self.datetime = datetime
        self.year = int(datetime[:4])
        self.month = int(datetime[5:7])
        self.day = int(datetime[8:10])
        
        self.hour = int(datetime[11:13])
        self.minute = int(datetime[14:16])
        self.second = int(datetime[17:19])
        
        self.value = value
    
    def __repr__(self):
        return '(' + self.datetime + ', Value: ' + str(self.value) + ')'
