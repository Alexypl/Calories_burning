import pandas as pd
import numpy as np

calories = pd.read_csv('calories.csv')

import plotly.express as px

fig = px.scatter(calories, x = 'Duration', y = "Calories", color = "Gender")
fig.show()