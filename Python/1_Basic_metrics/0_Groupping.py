import pandas as pd

calories = pd.read_csv('calories.csv')

metrics_by_age = calories.drop(columns = ['User_ID', 'Duration', 'Heart_Rate', 'Body_Temp', 'Calories', 'Age'])

print(metrics_by_age.groupby('Gender').agg(['mean', 'std', 'min', 'max']))