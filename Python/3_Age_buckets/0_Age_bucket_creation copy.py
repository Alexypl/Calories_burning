import pandas as pd
import numpy as np
import math

calories = pd.read_csv('calories.csv')

min_age = np.min(calories['Age'])
print("Mininum_age:", np.min(calories['Age']))

max_age = np.min(calories['Age'])
print("Maximum_age:", np.max(calories['Age']))

num_buckets = 10 # how many buckets we want to present
baskets = np.linspace(min_age, min_age+1, num_buckets) 

labels = []
ix = 0
for i in baskets:
    try:
        if math.ceil(baskets[ix]) == math.floor(baskets[ix]):
            if ix == 0:
                string = str(math.ceil(baskets[ix])) + "-" + str(math.floor(baskets[ix+1]))
                print(string)
                ix += 1
                labels.append(string)
            else:
                string = str(math.ceil(baskets[ix]) + 1) + "-" + str(math.floor(baskets[ix+1]))
                print(string)
                ix += 1
                labels.append(string)
        else:
            string = str(math.ceil(baskets[ix])) + "-" + str(math.floor(baskets[ix+1]))
            print(string)
            ix += 1
            labels.append(string)
    except IndexError:
        pass

calories['Age_bucket'] = pd.cut(calories['Age'], bins = len(labels), labels = labels)

