import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import scipy.stats as stats
import statsmodels.api as sm

calories = pd.read_csv('calories.csv')

duration_vs_calories = sm.OLS(y_train, X_train).fit()
print(duration_vs_calories.summary())