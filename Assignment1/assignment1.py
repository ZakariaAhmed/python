import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.ticker as ticker 
import datetime as dt 
import matplotlib.dates as mdates 

# indlæs data
allStocks = pd.read_csv("sandp500/all_stocks_5yr.csv")

# print alle kolonner
allColumns = allStocks.columns

# hent alle unikke navne, dvs henter alle de forskellige aktiers navne
stockNames = allStocks.Name.unique()
