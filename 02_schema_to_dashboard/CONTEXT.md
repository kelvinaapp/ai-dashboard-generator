# Stage 02: Business Metric & Transformation Engine

## Document Status
Living Document (Diperbarui jika ada penyesuaian rumus atau penambahan metrik turunan).

## Purpose
Mengolah `data_schema.xlsx` dari Stage 01 untuk menghitung seluruh KPI, agregasi bisnis, metrik turunan, serta menentukan indikator status RAG.

## Input & Output Surface
* **Input File:** `../01_raw_to_schema/output/data_schema.xlsx`
* **Script Executor:** `etl_transformer.py`
* **Output File:** `./output/data_ready.xlsx`

## Mandatory Metrics Checklist
* **Sales & Achievement:** Trend Sell Out (harian/mingguan/bulanan), Achievement MTD %, Achievement Full Month %.
* **Store Health:** Total Store, Total EC (Effective Calls), Productivity Rate %, Klasifikasi Store (Productive vs Non-Productive).
* **Inventory & Display:** Out of Stock (OOS) %, Weeks of Stock (WOS), Display Compliance Rate %.
* **Field Ops & Efficiency:** Grading Promoter (Grade A: >=100%, Grade B: 85-99%, Grade C: 70-84%, Grade D: <70%), Cost Ratio %.
* **Status Flags (RAG):** Green (>=95%), Yellow (80-94%), Red (<80%).
* **Anomaly Rule:** Capping Achievement maksimal di angka `200%`.

## Operating Rules
1. **Data Inspection:** Periksa ketersediaan kolom di `data_schema.xlsx` dan petakan ke rumus metrik wajib.
2. **Human-in-the-Loop Constraint:** DILARANG membuat `etl_transformer.py` atau me-run script sebelum rumus dan struktur tabel agregasi disetujui oleh User/PM.