#!/usr/bin/env python
# coding: utf-8

import pandas as pd, numpy as np
import sys
from joblib import dump

sys.set_int_max_str_digits(1000000000)
data = pd.read_csv("data/prem_i.csv", sep = ";")
data = data.dropna()
x = data.drop("target", axis = 1)
y = data["target"]


from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.45)
model = RandomForestRegressor(n_jobs = -1, random_state = 42, verbose = 2)
model.fit(x_train, y_train)
def predict(x): return model.predict(np.array([[x]]))[0]

print(list(map(predict, (23, 24, 25))))
model.score(x_test, y_test)

dump(model, "Models/Prem_i.pkl")