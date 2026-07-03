import pandas as pd
import joblib
import numpy as np

model = joblib.load("model/diabetes_model.pkl")

print("====================================")
print("    DIABETES PREDICTION SYSTEM")
print("====================================")
print("Please enter the patient's details.\n")

pregnancies = int(input("Enter Pregnancies: "))
glucose = float(input("Enter Glucose Level: "))
blood_pressure = float(input("Enter Blood Pressure: "))
skin_thickness = float(input("Enter Skin Thickness: "))
insulin = float(input("Enter Insulin Level: "))
bmi = float(input("Enter BMI: "))
diabetes_pedigree = float(input("Enter Diabetes Pedigree Function: "))
age = int(input("Enter Age: "))

user_data = pd.DataFrame([{
    "Pregnancies": pregnancies,
    "Glucose": glucose,
    "BloodPressure": blood_pressure,
    "SkinThickness": skin_thickness,
    "Insulin": insulin,
    "BMI": bmi,
    "DiabetesPedigreeFunction": diabetes_pedigree,
    "Age": age
}])

prediction = model.predict(user_data)

print("\n====================================")

if prediction[0] == 1:
    print("Prediction Result")
    print("The person is likely to have Diabetes.")
else:
    print("Prediction Result")
    print("The person is NOT likely to have Diabetes.")

print("====================================")