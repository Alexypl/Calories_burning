import pandas as pd
import numpy as np
import math

calories = pd.read_csv('calories.csv')

# which endogenous variable influences the calories burning the most
columns_to_check = ['Height', 'Weight', 'Duration', 'Heart_Rate', 'Body_Temp']

def reg_plot_with_rsquared(data, x, y, **kwargs):
    sns.regplot(data = data, x = x, y = y, scatter = True, line_kws={"color": "red"}, **kwargs)
    slope, intercept, r_value, p_value, std_err = stats.linregress(data[x], data[y])
    r_squared = r_value**2
    ax = plt.gca()
    ax.text(0.05, 0.9, f'R² = {r_squared:.2f}', transform=ax.transAxes, fontsize=12, color='blue')

for column in columns_to_check:
    if column in ['Height', 'Weight']:
        g = sns.FacetGrid(calories)
        g.map_dataframe(reg_plot_with_rsquared, x = column, y = 'Calories')
    else:
        g = sns.FacetGrid(calories)
        g.map_dataframe(reg_plot_with_rsquared, x = column, y = 'Calories', order = 2)


