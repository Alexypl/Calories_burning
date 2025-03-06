import pandas as pd
import numpy as np

calories = pd.read_csv('calories.csv')

def reg_plot_with_rsquared(data, x, y, **kwargs):
    sns.scatterplot(data = data, x = x, y = y, **kwargs)
    
g = sns.FacetGrid(calories, col="Age_bucket", col_wrap=3)
g.map_dataframe(reg_plot_with_rsquared, x = 'Duration', y = 'Calories')