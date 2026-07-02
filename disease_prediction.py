import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

print("Libraries Imported Successfully")
data = pd.read_csv("dataset/diabetes.csv")
print(data.head())

print("\nShape of Dataset:")
print(data.shape)
print("\nColumns Names:")
print(data.columns)
print("\nDataset Information:")
print(data.info())
print("\nMissing Values:")
print(data.isnull().sum())
print("\nStatistical Summary:")
print(data.describe())

X = data.drop("Outcome", axis=1)
y = data["Outcome"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)
model=LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
prediction = model.predict(X_test)
accuracy = accuracy_score(y_test, prediction)
print("Model Accuracy:", accuracy)
joblib.dump(model,"model/diabetes_model.pkl")
print("Model Saved Successfully")