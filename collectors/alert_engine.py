from collectors.slow_queries import fetch_slow_queries
from collectors.table_health import fetch_table_bloat_and_stats

def run_health_checks():
    
    print("\n🔍 [BACKGROUND CHECK] Veritabanı sağlık kontrolü başlatıldı...")
    
   
    slow_queries = fetch_slow_queries(threshold_seconds=2)
    if slow_queries:
        print(f"⚠️ UYARI: {len(slow_queries)} adet yavaş sorgu tespit edildi!")
        for q in slow_queries:
            print(f"   ---> [PID: {q['pid']}] Kullanıcı: {q['user_name']} | Süre: {q['duration']} | Sorgu: {q['query'][:50]}...")
    else:
        print("✅ Yavaş çalışan kritik sorgu bulunamadı.")

  
    table_stats = fetch_table_bloat_and_stats()
    critical_tables = [t for t in table_stats if t['dead_row_percent'] > 20.0]
    
    if critical_tables:
        print(f"⚠️ UYARI: {len(critical_tables)} tabloda kritik ölü satır oranı (%20 üzeri) tespit edildi!")
        for t in critical_tables:
            print(f"   ---> Tablo: {t['schema']}.{t['table_name']} | Ölü Satır Oranı: %{t['dead_row_percent']} | VACUUM Gerekebilir.")
    else:
        print("✅ Tablo ölü satır oranları güvenli seviyede.")