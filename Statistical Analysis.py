#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 22:57:58 2024

@author: khushiwadhwani
"""

pip install scikit-learn


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder

file_path = '/Users/khushiwadhwani/desktop/cleaned_marketing_campaign_dataset.csv'


df = pd.read_csv(file_path)

df['Acquisition_Cost'] = df['Acquisition_Cost'].replace({'\$': '', ',': ''}, regex=True).astype(float)


le = LabelEncoder()
df['Company'] = le.fit_transform(df['Company'])
df['Campaign_Type'] = le.fit_transform(df['Campaign_Type'])
df['Channel_Used'] = le.fit_transform(df['Channel_Used'])
df['Location'] = le.fit_transform(df['Location'])
df['Language'] = le.fit_transform(df['Language'])
df['Customer_Segment'] = le.fit_transform(df['Customer_Segment'])

X = df[['Company', 'Campaign_Type', 'Duration (in days)', 'Channel_Used', 
        'Conversion_Rate', 'Acquisition_Cost', 'ROI', 'Location', 'Language', 
        'Clicks', 'Impressions', 'Engagement_Score', 'Customer_Segment']]
y = df['ROI']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

# c. Evaluate the model on the test set
y_pred = model.predict(X_test)

# d. Calculate MSE and R²
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error (MSE): {mse}")
print(f"Coefficient of Determination (R²): {r2}")

