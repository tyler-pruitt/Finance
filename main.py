#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 16:57:14 2022

@author: tylerpruitt
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from objects import StockData

data = np.loadtxt("ticker.csv", dtype=str, delimiter=',')

dataArray = np.empty(len(data)-1, dtype=StockData)

for i in range(1, len(data)):
    dataArray[i-1] = StockData(data[i,0], float(data[i,1]), float(data[i,2]), float(data[i,3]), float(data[i,4]), float(data[i,5]), float(data[i,6]), data[i,7])