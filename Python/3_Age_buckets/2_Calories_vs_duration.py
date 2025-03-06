import pandas as pd
import numpy as np

calories = pd.read_csv('calories.csv')

for bucket in calories['Age_bucket'].unique():
    y = calories[calories['Age_bucket'] == bucket]['Calories']
    x = calories[calories['Age_bucket'] == bucket]['Duration']
    plt.scatter(x, y)
    plt.title(f'Duration vs Calories in age bucket: {bucket}')
    plt.show()