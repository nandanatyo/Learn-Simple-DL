import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model

# Load model yang sudah disimpan
model = load_model("diabetes_model.h5")

# Contoh data baru (format sesuai dataset: 8 kolom input)
# urutannya: Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age
new_data = np.array([[2, 120, 70, 25, 80, 28.5, 0.3, 35]])

# Prediksi
prob = model.predict(new_data)
print("Probabilitas:", prob)
print("Prediksi:", 1 if prob > 0.5 else 0)
