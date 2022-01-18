import inline as inline
import matplotlib
import pylab
import calendar
import numpy as np
import pandas as pd
import seaborn as sn
from scipy import stats
import missingno as msno
from datetime import datetime
import matplotlib.pyplot as plt
import warnings
pd.options.mode.chained_assignment = None
warnings.filterwarnings("ignore", category=DeprecationWarning)
#matplotlib inline

path = "/Users/rangxiao/Downloads"
dailyData = pd.read_csv(path)
dailyData.shape
