import pandas as pd
import numpy as np
import seaborn as sns

# import matplotlib.pyplot as plt
# %matplotlib inline
import warnings
warnings.filterwarnings('ignore')
# indlæs data
fifadata = pd.read_csv("FIFA2018Statistics.csv")

# numerisk features
numerisk_features = fifadata.select_dtypes(include = [np.number]).columns
# af kategori
kategorisk_features = fifadata.select_dtypes(include= [np.object]).columns

# data beskrivelse
databeskrivelse = fifadata.describe()

# Vi kan plotte med matplotlib 
# fifadata.hist(figsize=(30,30))
# grafer = plt.plot()
# plt.show
