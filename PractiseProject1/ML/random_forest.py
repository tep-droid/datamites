import pandas as pd
import numpy as np

df = pd.read_csv("synthetic_resume_data.csv")

print(df.describe())

# Scaling
x = df.iloc[:, :-1]
from sklearn.preprocessing import MinMaxScaler
mm = MinMaxScaler()
scaled = mm.fit_transform(x)
X = pd.DataFrame(scaled, columns = df.columns[:-1])

# Already preproceesed data -> no null values, all numerical columns, scaling done

# movong to corelation
## Checking mulicollinearity
res = X[X.columns].corr()

# Checking colineraity
res[res > 0.8]
print(res)

# since num_matched_skills and resume_score_raw -> colinearity = 1.000, removing resume_raw_score
X = X.drop(columns=['resume_score_raw'])


# To check colinearity using matplotlib

X['score_percentage'] = df['score_percentage']
# ## Checking correlation after normalizing
# plt.figure(figsize=(20,25))
# sns.heatmap(X.corr(), annot = True)

# Creating independent and dependent variable
X = X.drop('score_percentage', axis = 1)
y = df['score_percentage']

# Creating training and testing data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, train_size = 0.80, random_state = 42)

# Building model
from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Metrics calculation
from sklearn.metrics import *
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("RMSE: ", rmse)
print("R2 score: ", r2)


# Comparing model with dummy regressor

from sklearn.dummy import DummyRegressor
dummy_model = DummyRegressor(strategy="mean")
dummy_model.fit(X_train, y_train)

y_dummy_pred = dummy_model.predict(X_test)

dummy_rmse = np.sqrt(mean_squared_error(y_test, y_dummy_pred))
dummy_r2 = r2_score(y_test, y_dummy_pred)

print("Dummy RMSE:", dummy_rmse)
print("Dummy R2:", dummy_r2)

# 1️⃣ Dummy baseline behaves exactly as expected ✅
#
# R² ≈ 0 or negative → predicts mean → useless model
#
# RMSE is very high → huge average error

# 2️⃣ Random Forest massively outperforms baseline ✅
#
# RMSE improved by ~5×
#
# R² jumped from ~0 → ~0.96

###“Compared to a naive mean predictor, our Random Forest model significantly improves prediction accuracy,
# demonstrating that engineered resume features capture meaningful relationships with resume–JD match scores.”

# comparing with linear regression

from sklearn.linear_model import LinearRegression
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)


y_lr_pred = lr_model.predict(X_test)

lr_rmse = np.sqrt(mean_squared_error(y_test, y_lr_pred))
lr_r2 = r2_score(y_test, y_lr_pred)

print("Linear Regression RMSE:", lr_rmse)
print("Linear Regression R2:", lr_r2)

# Save the model

import pickle

with open('my_model.pkl', 'wb') as f:
    pickle.dump(model, f)

## Load the model
# with open('my_model.pkl', 'rb') as f:
#     loaded_model = pickle.load(f)