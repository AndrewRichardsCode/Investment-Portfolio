# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 12:48:21 2020

@author: Andrew Richards
"""

import numpy as np
import pandas as pd
from datetime import datetime
import quandl
quandl.ApiConfig.api_key = ""

class portfolio:
    
    tickers = []
    weights = []
    start = datetime(1995, 1, 1)
    #end = datetime.datetime(2019, 1, 27)
    rawData = pd.DataFrame()
    
    def __init__(self, tickers, weights):
        self.tickers = tickers
        self.weights = np.array(weights)
        for t in self.tickers:
            self.rawData[t] = quandl.get(t, start_date=self.start)['Adj. Close']
            
    
    
    def calcReturn(self):
        simpleDailyReturns = (self.rawData / self.rawData.shift(1)) - 1
        #logDailyReturns = np.log(1 + self.rawData.pct_change())
        annualAvgReturns = simpleDailyReturns.mean() * 250 
        return np.dot(annualAvgReturns, self.weights)
        
    def calcVariance(self):
        simpleDailyReturns = (self.rawData / self.rawData.shift(1)) - 1
        #logDailyReturns = np.log(1 + self.rawData.pct_change())
        return np.dot(self.weights.T, np.dot(simpleDailyReturns.cov() * 250, self.weights))
    
    def calcVolatility(self):
        return self.calcVariance() ** 0.5
    
    def printReturns(self):
        print('Annual Portfolio Return: ' + str(round(self.calcReturn()*100, 3)) + '%')
    
    def printRisk(self):
        print(str(round(self.calcVariance()*100, 3)) + '% Portfolio Variance')
        print(str(round(self.calcVolatility()*100, 3)) + '% Portfolio Volatility')
    
    def overview(self):
        self.printReturns()
        self.printRisk()
















