# Libraries
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pandas as pd
from time import time
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import FeatureUnion
from sklearn.linear_model.logistic import LogisticRegression

# Globals
file_dir = './data/sleep/'
start = time()
header=[0]

# Import train data
jun = pd.read_csv('{0}6 - June.csv'.format(file_dir), skiprows=header)
jul = pd.read_csv('{0}7 - July.csv'.format(file_dir), skiprows=header)
aug = pd.read_csv('{0}8 - August.csv'.format(file_dir), skiprows=header)
sep = pd.read_csv('{0}9 - September.csv'.format(file_dir), skiprows=header)
oct = pd.read_csv('{0}10 - October.csv'.format(file_dir), skiprows=header)
nov = pd.read_csv('{0}11 - November.csv'.format(file_dir), skiprows=header)

year_2015 = [jun,jul,aug,sep,oct,nov]
data = pd.concat(year_2015)

print(data)

# Done
print('Finished. Script ran in {0} seconds'.format(time() - start))


