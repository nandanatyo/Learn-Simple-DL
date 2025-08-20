# 🧠 Deep Learning Sederhana – Pima Indians Diabetes

Proyek ini adalah contoh **model deep learning sederhana** menggunakan **Python + TensorFlow/Keras** untuk memprediksi apakah seorang pasien menderita diabetes atau tidak, berdasarkan dataset **Pima Indians Diabetes**.

## 📂 Dataset

Dataset: `diabetes.csv`
Kolom-kolom:

* `Pregnancies` → jumlah kehamilan
* `Glucose` → kadar gula darah
* `BloodPressure` → tekanan darah
* `SkinThickness` → ketebalan lipatan kulit
* `Insulin` → kadar insulin
* `BMI` → indeks massa tubuh
* `DiabetesPedigreeFunction` → riwayat diabetes dalam keluarga
* `Age` → umur
* `Outcome` → label (0 = tidak diabetes, 1 = diabetes)

⚠️ File CSV ini memiliki **header**, jadi kita pakai `pandas` agar mudah membacanya.

---

## ⚙️ Instalasi

1. Clone repo ini (atau download file Python + CSV).

   ```bash
   git clone <hehe>
   cd <hehe>
   ```

2. Buat virtual environment (opsional tapi disarankan).

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. Install dependencies.

   ```bash
   pip install tensorflow pandas numpy
   ```

---

## 📝 Cara Menjalankan

1. Pastikan file `diabates.csv` ada di folder project.
2. Jalankan `python diabetes.py`

---

## 📊 Hasil

* **Loss** → ukuran error (semakin kecil semakin bagus).
* **Accuracy** → persentase prediksi benar.

Contoh output:

```
Epoch 150/150
768/768 [==============================] - 0s 1ms/step - loss: 0.4800 - accuracy: 0.7708
Loss: 0.4800, Accuracy: 0.7708
Probabilitas: [[0.84]] Prediksi: 1
```

---

## 📖 Istilah Penting

* **Epoch** → berapa kali seluruh dataset dipelajari ulang.
* **Batch size** → jumlah data yang diproses tiap langkah.
* **Loss** → angka kesalahan prediksi.
* **Accuracy** → tingkat ketepatan model.
* **Activation function** → fungsi matematika agar model bisa memahami pola non-linear.
* **Optimizer** → algoritma untuk mempercepat dan menstabilkan pembelajaran.

---

## 🚀 Next Step

* Coba ubah jumlah layer/neuron.
* Coba dataset lain (misalnya MNIST untuk gambar angka).
* Coba *train/test split* (bagi data jadi 80% training, 20% testing).
