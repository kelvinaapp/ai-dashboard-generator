# Tujuan Stage 03: HTML Generation
Tugas kamu adalah membuat file HTML *offline* yang bisa dibuka melalui email. 
Gunakan Jinja2 di `generate_html.py` untuk membaca tabel dari `data_ready.xlsx`, mengubahnya menjadi format JSON/Dictionary, dan menginjeksikannya ke dalam `template.html`.

**Aturan UI/UX:**
1. Gunakan Tailwind CSS via CDN untuk styling.
2. Gunakan Chart.js via CDN untuk visualisasi chart dasar (Bar/Pie Chart).
3. File final `dashboard_final.html` tidak boleh memanggil aset CSS/JS lokal (semua harus CDN atau inline).