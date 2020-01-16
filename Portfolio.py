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
    
    def calcAssetReturn(self):
        simpleDailyReturns = (self.rawData / self.rawData.shift(1)) - 1
        return simpleDailyReturns.mean() * 250
    
    def calcAssetVariance(self):
        simpleDailyReturns = (self.rawData / self.rawData.shift(1)) - 1
        return simpleDailyReturns.var() * 250
        
    def calcVariance(self):
        simpleDailyReturns = (self.rawData / self.rawData.shift(1)) - 1
        #logDailyReturns = np.log(1 + self.rawData.pct_change())
        return np.dot(self.weights.T, np.dot(simpleDailyReturns.cov() * 250, self.weights))
    
    def calcVolatility(self):
        return self.calcVariance() ** 0.5
    
    def divRisk(self):
        assetVar = self.calcAssetVariance()
        portVar = self.calcVariance()
        for t in range(len(self.tickers)):
            portVar -= (self.weights[t] ** 2 * assetVar[t])
        return portVar
    
    def nonDivRisk(self):
        return self.calcVariance() - self.divRisk()
    
    def printPortfolioReturn(self):
        print('Portfolio Return:        ' + str(round(self.calcReturn()*100, 3)) + '%')
        
    def printAssetReturns(self):
        returns = round(self.calcAssetReturn()*100, 3)
        returns = pd.DataFrame(returns)
        returns.columns = ['Return']
        pd.options.display.float_format = '{:}%'.format
        print(returns.to_string())
        
    def printAssetVariance(self):
        var = round(self.calcAssetVariance()*100, 3)
        var = pd.DataFrame(var)
        var.columns = ['Variance']
        pd.options.display.float_format = '{:}%'.format
        print(var.to_string())
        
    
    def printRisk(self):
        print('Portfolio Variance:      ' + str(round(self.calcVariance()*100, 3)) + '%')
        print('Portfolio Volatility:    ' + str(round(self.calcVolatility()*100, 3)) + '%')
        print('Diversifiable Risk:      ' + str(round(self.divRisk()*100, 3)) + '%')
        print('Non-Diversifiable Risk:  ' + str(round(self.nonDivRisk()*100, 3)) + '%')
    
    def overview(self):
        self.printPortfolioReturn()
        self.printRisk()
        print()
        self.printAssetReturns()
        print()
        self.printAssetVariance()
















