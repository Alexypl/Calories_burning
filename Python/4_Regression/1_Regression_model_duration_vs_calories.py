import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import scipy.stats as stats

calories = pd.read_csv('calories.csv')

duration_vs_calories = LinearRegression().fit(calories[['Duration']], calories['Calories'])

print("Coeficient:",duration_vs_calories.coef_)
print("Intercept:", duration_vs_calories.intercept_)

y_pred = model.predict(duration_vs_calories[['Duration']])

print("R_squared:", r2_score(calories['Calories'], y_pred))