import tkinter as tk
import joblib
import pandas as pd

model = joblib.load("model/diabetes_model.pkl")

root = tk.Tk()

root.title("Diabetes Prediction System")
root.geometry("500x600")
root.resizable(False, False)
root.configure(bg="#E7F7F7")

title = tk.Label(
    root,
    text="Diabetes Prediction System",
    font=("Arial", 18, "bold"),
    bg="#EAF6F6",
    fg="darkblue"
)

title.pack(pady=20)
labels = [
    "Pregnancies",
    "Glucose",
    "Blood Pressure",
    "Skin Thickness",
    "Insulin",
    "BMI",
    "Diabetes Pedigree",
    "Age"
]

entries = []

for text in labels:
    tk.Label(root, text=text, bg="lightblue", font=("Arial", 11)).pack()

    entry = tk.Entry(root, width=30)
    entry.pack(pady=3)

    entries.append(entry)


    def predict():
        try:
            pregnancies = int(entries[0].get())
            glucose = float(entries[1].get())
            blood_pressure = float(entries[2].get())
            skin_thickness = float(entries[3].get())
            insulin = float(entries[4].get())
            bmi = float(entries[5].get())
            pedigree = float(entries[6].get())
            age = int(entries[7].get())

            user_data = pd.DataFrame([{
                "Pregnancies": pregnancies,
                "Glucose": glucose,
                "BloodPressure": blood_pressure,
                "SkinThickness": skin_thickness,
                "Insulin": insulin,
                "BMI": bmi,
                "DiabetesPedigreeFunction": pedigree,
                "Age": age
            }])

            prediction = model.predict(user_data)

            if prediction[0] == 1:
                result.config(
                    text="⚠ Diabetes Detected",
                    fg="red"
                )
            else:
                result.config(
                    text="✓ No Diabetes",
                    fg="green"
                )

        except:
            result.config(
                text="Please enter valid values",
                fg="orange"
            )
button = tk.Button(
    root,
    text="Predict",
    command=predict,
    bg="green",
    fg="white",
    font=("Arial", 12, "bold"),
    width=20
)

button.pack(pady=15)
result = tk.Label(
    root,
    text="",
    bg="lightblue",
    font=("Arial", 13, "bold")
)

result.pack(pady=10)
root.mainloop()