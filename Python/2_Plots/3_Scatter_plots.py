import pandas as pd
import numpy as np

calories = pd.read_csv('calories.csv')

for column in calories.columns:
    if column in ['User_ID', 'Calories', 'Gender']:
        pass
    elif calories[column].dtype == 'int64' or calories[column].dtype == 'float64':
        plt.figure()
        sns.scatterplot(data = calories, x = column, y = 'Calories', hue = 'Gender')
        plt.show()