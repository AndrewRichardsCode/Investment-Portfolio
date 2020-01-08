# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 12:48:21 2020

@author: Andrew Richards
"""

import numpy as np
import pandas as pd
import datetime
import quandl
quandl.ApiConfig.api_key = ""

class portfolio:
    
    assets = []
    weights = []
    
    def __init__(self, tickers, weights):
        self.assets = tickers
        self.weights = weights
        
    def initData():
        return 0

    def calcReturn():
        return 0
        
    def calcRisk():
        return 0
    
    def printReturn():
        return 0
    
    def printRisk():
        return 0
    
    def overview():
        return 0
















