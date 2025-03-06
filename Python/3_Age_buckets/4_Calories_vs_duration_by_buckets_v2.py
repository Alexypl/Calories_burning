import pandas as pd
import numpy as np

calories = pd.read_csv('calories.csv')

def reg_plot_with_rsquared(data, x, y, **kwargs):
    sns.regplot(data = data, x = x, y = y, scatter = True, line_kws={"color": "red"}, **kwargs)
    slope, intercept, r_value, p_value, std_err = stats.linregress(data[x], data[y])
    r_squared = r_value**2
    ax = plt.gca()
    ax.text(0.05, 0.9, f'R² = {r_squared:.2f}', transform=ax.transAxes, fontsize=12, color='blue')
    
g = sns.FacetGrid(calories, col="Age_bucket", col_wrap=3)
g.map_dataframe(reg_plot_with_rsquared, x = 'Duration', y = 'Calories', order = 2)