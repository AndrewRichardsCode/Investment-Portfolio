# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 12:47:43 2020

@author: Andrew Richards
"""

from Portfolio import portfolio


tickers = ['WIKI/MSFT', 'WIKI/T', 'WIKI/F', 'WIKI/GE']
weights = [0.25, 0.25, 0.25, 0.25]

portfolio1 = portfolio(tickers, weights)
portfolio1.overview()

test = portfolio1.divRisk()

