# Enterprise Database Observability & Health Operations Suite 🚀

PostgreSQL veritabanı performansını, yavaş çalışan sorguları, tablo ölü satır oranlarını (bloat) ve kullanılmayan indeksleri anlık olarak izleyen ve otomatik ikazlar üreten **Python & FastAPI** tabanlı izleme servisi.

---

## 🎯 Projenin Öne Çıkan Özellikleri

- **Slow Query Monitor:** PostgreSQL `pg_stat_activity` kataloğunu analiz ederek belirlenen eşik değerinden (threshold) uzun süren ve CPU/RAM tüketen aktif sorguları tespit eder.
- **Table Health & Bloat Detection:** `pg_stat_user_tables` üzerindeki ölü satır (dead tuple) oranlarını hesaplayarak `VACUUM` bakımı gereken tabloları raporlar.
- **Index Optimization Engine:** Veritabanında disk alanı kaplayan ancak kullanılmayan atıl indeksleri (`pg_stat_user_indexes`) tespit eder.
- **Automated Background Alerts:** `APScheduler` ile 30 saniyelik periyotlarla arka planda veritabanı sağlığını denetler ve kritik durumlarda uyarı fırlatır.
- **Swagger REST API:** Tüm gözlemlenebilirlik verilerini temiz ve standart bir API mimarisi ile sunar.

---

## 🛠️ Teknoloji Yığını

- **Dil:** Python 3.12+
- **Framework:** FastAPI, Uvicorn
- **Veritabanı Sürücüsü:** Psycopg2 (RealDictCursor)
- **Zamanlayıcı:** APScheduler
- **Veritabanı:** PostgreSQL

---

## 🚀 Kurulum ve Çalıştırma

1. **Sanal ortamı oluşturun ve aktif edin:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Windows için: .\venv\Scripts\Activate.ps1