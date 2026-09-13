# Tujuan Stage 02: Schema to Dashboard Data
Tugas kamu adalah membaca `data_schema.xlsx` dari folder output tahap 01, lalu melakukan agregasi data yang siap ditampilkan di dashboard.

**Aturan Kalkulasi:**
1. Lakukan Grouping berdasarkan Kategori atau Area (sesuaikan dengan data).
2. Hitung persentase pencapaian (*Achievement* = Aktual / Target).
3. Jika ada angka *growth* atau pencapaian yang anomali (misal > 200%), pastikan tidak merusak kalkulasi total (terapkan capping jika diperlukan).
4. Simpan hasilnya ke `output/data_ready.xlsx`.