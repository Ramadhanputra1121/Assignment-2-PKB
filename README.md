# Assignment-2-PKB

# Nama Kelompok
    1. Digra Murtaza Izham - 1313621010
    2. Faizal Rizqi Kholily - 1313621029
    3. Muhammad Ramadhan Putra Pratama - 1313621038
    4. Rasyaad Maulana Khandiyas - 1313621020

# Cara Kerja
## predictOnly.py
    1. Input data baru disertai dengan sepallength, sepalwidth, petallength, petalwidth
    2. Width dari data yang sudah tersedia kemudian dihitung rata-ratanya dan disimpan di variabel "averages"
    3. Length dari data yang sudah tersedia kemudian dihitung rata-ratanya dan disimpan di variabel "averages"
    4. Dilakukan operasi ("sepalwidth" * "averages" + "sepallength" * "averages" + "petalwidth" * "averages" + "petallength" * "averages) = "new_score"
    5. Setiap row dari data yang sudah ada dilakukan operasi yang sama dengan hasil akhir "existing_score"
    6. Setelah mendapatkan hasil "new_score" dan "existing_score" dari setiap row, dilakukan operasi distance = abs("new_score" - "existing_score") yang dilakukan berulang di setiap row yang ada.
    7. Selisih paling minimum diantara "new_score" - "existing_score" dijadikan acuan class untuk data baru.

## accuracyOnly.py
    1. "read_file = pd.read_csv('iris.csv'): Kode ini membaca dataset iris dari file CSV dengan nama 'iris.csv' dan menyimpannya dalam bentuk DataFrame dengan nama 'read_file'.
    2. def calculate_score(data, averages): Ini adalah definisi fungsi calculate_score() yang mengambil data (seperti panjang dan lebar sepal serta panjang dan lebar petal) dan nilai rata-rata sebagai argumen, dan menghitung skor berdasarkan produk skalar antara data dan nilai rata-rata.
    3. def predict_species(data, training_data, averages): Ini adalah definisi fungsi predict_species() yang digunakan untuk memprediksi spesies bunga iris berdasarkan data yang diberikan. Fungsi ini menggunakan nilai rata-rata yang telah dihitung sebelumnya untuk mencari spesies yang paling mirip dengan data yang diberikan dari data pelatihan.
    4. Selanjutnya, kita memisahkan fitur-fitur (X) dan label (y) dari DataFrame 'read_file' menggunakan iloc.
    5. X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.7, shuffle=True): Ini membagi data menjadi data pelatihan (X_train dan y_train) dan data pengujian (X_test dan y_test) dengan perbandingan 70:30, dan melakukan pengacakan data (shuffle=True).
    6. training_data = pd.concat([X_train, y_train], axis=1): Ini menggabungkan fitur-fitur dan label dari data pelatihan ke dalam satu DataFrame yang disebut training_data.
    7. averages = X_train.mean().tolist(): Ini menghitung nilai rata-rata dari setiap fitur di data pelatihan dan menyimpannya dalam bentuk daftar.
    8. y_pred = []: Ini membuat daftar kosong y_pred yang akan digunakan untuk menyimpan hasil prediksi.
    9. Di dalam loop for index, row in X_test.iterrows():, setiap baris dari data pengujian diambil satu per satu.
    10. data = row.tolist(): Data dari baris tersebut diubah menjadi daftar.
    11. predicted_species = predict_species(data, training_data, averages): Fungsi predict_species() dipanggil untuk memprediksi spesies berdasarkan data dari baris pengujian.
    12. Hasil prediksi (spesies) disimpan dalam daftar y_pred.
    13. Setelah loop selesai, akurasi prediksi dihitung dengan membandingkan y_test (label sebenarnya) dengan y_pred (hasil prediksi) menggunakan fungsi accuracy_score.
    14. Hasil akurasi dicetak ke layar dalam format persentase. Akurasi ini mengukur seberapa baik model klasifikasi ini dapat memprediksi spesies bunga iris berdasarkan nilai rata-rata dari fitur-fitur yang ada dalam dataset.