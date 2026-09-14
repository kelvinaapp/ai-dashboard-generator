# Stage 03: Offline HTML Dashboard Generator

## Document Status
Living Document (Diperbarui berdasarkan penyesuaian tata letak UI atau komponen visual).

## Purpose
Membaca data dari `data_ready.xlsx`, mengonversinya menjadi data JSON, dan merender dashboard interaktif *standalone* yang siap dibuka secara *offline*.

## Input & Output Surface
* **Input File:** `../02_schema_to_dashboard_data/output/data_ready.xlsx`
* **Template File:** `template.html`
* **Script Executor:** `generate_html.py`
* **Output File:** `./output/dashboard_final.html`

## Technical & Visual Specifications
* **Theme (Samsung Palette):**
  - Background Utama: Light Gray (`#F8F9FA`)
  - Background Card: Pure White (`#FFFFFF`)
  - Teks & Heading: Dark Slate / Black (`#111111`)
  - Aksen Utama: Samsung Blue (`#1428A0` / `#0057B8`)
  - Badge Status RAG: Red (`#EF4444`), Yellow (`#F59E0B`), Green (`#10B981`)
* **Framework Stack (via CDN / Inline):** Tailwind CSS, Chart.js / ECharts. Dilarang menggunakan dependensi file `.css`/`.js` lokal.
* **Offline Interactivity (Vanilla JS):**
  - Dropdown Filter untuk Region/Area dan Bulan.
  - Search Bar interaktif untuk menyaring tabel detail toko.
  - Sorting otomatis pada kolom tabel detail.
* **Data Ingestion:** Menggunakan Jinja2 di `generate_html.py` untuk menyisipkan JSON langsung ke tag `<script>` HTML.

## Operating Rules
1. **Wireframe First:** Tampilkan rancangan susunan komponen visual ke terminal sebelum coding.
2. **Human-in-the-Loop Constraint:** DILARANG mengubah `template.html` atau me-run `generate_html.py` sebelum wireframe disetujui oleh User/PM.