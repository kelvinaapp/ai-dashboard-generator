# Stage 01: Raw Data Exploration & Schema Standardization

## Document Status
Living Document (Diperbarui oleh AI/PM setelah eksplorasi data mentah selesai dan disetujui User).

## Purpose
Membaca seluruh file Excel di `./data_raw/`, mengeksplorasi struktur data asli, serta menyusun skema data tunggal yang terintegrasi, bersih, dan konsisten.

## Input & Output Surface
* **Input Directory:** `./data_raw/` (berisi kumpulan file Excel mentah).
* **Script Executor:** `etl_cleaner.py`
* **Output File:** `./output/data_schema.xlsx`

## Operating Rules
1. **Multi-File Detection:** Sistem harus otomatis membaca semua file `.xlsx` / `.xls` di folder `./data_raw/`.
2. **Standardization Protocol:**
   - Penyeragaman header kolom menjadi `lowercase` dengan `underscore` (contoh: `Store Name` -> `store_name`).
   - Penyeragaman format tanggal ke `YYYY-MM-DD`.
   - Pembersihan duplikasi data berdasarkan kunci ID unik.
   - Handling nilai `NULL`/kosong pada angka kuantitatif (defaulting ke 0 jika relevan).
3. **Human-in-the-Loop Constraint:**
   - DILARANG membuat/menjalankan script `etl_cleaner.py` sebelum skema gabungan yang diusulkan mendapatkan persetujuan dari User/PM.