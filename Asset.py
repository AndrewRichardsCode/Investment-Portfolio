# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 13:25:24 2020

@author: Andrew Richards
"""
import numpy as np
import pandas as pd
import datetime
import quandl
quandl.ApiConfig.api_key = ""


class asset:
    
    ticker = 0
    
    def __init__(self, ticker):
        self.ticker = ticker
        
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
