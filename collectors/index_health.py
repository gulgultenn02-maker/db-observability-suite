from database import get_db_connection

def fetch_unused_indexes():
   
    query = """
        SELECT 
            schemaname AS schema,
            relname AS table_name,
            indexrelname AS index_name,
            idx_scan AS index_scans,
            pg_size_pretty(pg_relation_size(indexrelid)) AS index_size
        FROM pg_stat_user_indexes
        WHERE idx_scan = 0
          AND idx_relname NOT LIKE '%_pkey'
        ORDER BY pg_relation_size(indexrelid) DESC;
    """
    
    conn = get_db_connection()
    if not conn:
        return []
    
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        unused_indexes = cursor.fetchall()
        cursor.close()
        conn.close()
        
        return [dict(idx) for idx in unused_indexes]
    except Exception as e:
        print(f"❌ İndeks analiz hatası: {e}")
        if conn:
            conn.close()
        return []