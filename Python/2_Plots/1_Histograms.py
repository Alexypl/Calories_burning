import pandas as pd
import numpy as np

calories = pd.read_csv('calories.csv')

calories_hist = calories.drop(columns = ['User_ID'])

for column in calories_hist.columns:
    if calories[column].dtype == 'int64' or calories[column].dtype == 'float64':
        plt.figure()
        sns.histplot(calories, x = column)
        plt.title(column)
        plt.show()