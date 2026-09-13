# Tujuan Stage 01: Raw to Schema
Tugas kamu di folder ini adalah membaca `data_raw.xlsx` dan membersihkannya menjadi `data_schema.xlsx` di dalam folder `/output`.

**Aturan Pembersihan:**
1. Hapus baris yang kosong (Missing Values) pada kolom esensial (seperti ID Toko, Nama, Kategori).
2. Standarisasi format tanggal menjadi YYYY-MM-DD.
3. Pastikan tipe data kuantitatif (seperti target dan aktual) diformat sebagai numerik (Float/Integer).
4. Tulis hasil akhirnya menggunakan Pandas ke `output/data_schema.xlsx` tanpa menyertakan index.