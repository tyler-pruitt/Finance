#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 17:40:38 2022

@author: tylerpruitt
"""

class StockData(object):
    def __init__(self, datetime, openPrice, highPrice, lowPrice, closePrice, volume):
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
        self.volume = volume
