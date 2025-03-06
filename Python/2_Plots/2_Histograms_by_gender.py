import pandas as pd
import numpy as np

calories = pd.read_csv('calories.csv')

calories_hist = calories.drop(columns = ['User_ID'])


for column in calories_hist.columns:
    if column in ['User_ID', 'Gender']:
        pass
    elif calories_hist[column].dtype == 'int64' or calories_hist[column].dtype == 'float64':
        plt.figure()
        g = sns.FacetGrid(calories, col = 'Gender')
        g.map(sns.histplot, column)
        plt.show()