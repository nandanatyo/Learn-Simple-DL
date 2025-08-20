from numpy import loadtxt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Load data
data = loadtxt('diabetes.csv', delimiter=',')
X, y = data[:, :-1], data[:, -1]

# Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,Outcome

# Definisikan model
model = Sequential([
    Dense(12, input_shape=(X.shape[1],), activation='relu'),
    Dense(8, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Kompilasi model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Latih model
model.fit(X, y, epochs=150, batch_size=10, verbose=1)

# Evaluasi
loss, accuracy = model.evaluate(X, y)
print(f'Loss: {loss:.4f}, Akurasi: {accuracy:.4f}')

# Prediksi
prob = model.predict(X[0].reshape(1, -1))
print("Probabilitas:", prob, "— Prediksi:", 1 if prob > 0.5 else 0)

# Simpan model
model.save("diabetes_model.h5")
print("✅ Model berhasil disimpan sebagai diabetes_model.h5")
