from database import get_db_connection

def fetch_table_bloat_and_stats():
  
    query = """
        SELECT 
            schemaname AS schema,
            relname AS table_name,
            n_live_tup AS live_rows,
            n_dead_tup AS dead_rows,
            ROUND(
                (n_dead_tup::numeric / NULLIF(n_live_tup + n_dead_tup, 0)) * 100, 2
            ) AS dead_row_percent,
            last_vacuum,
            last_autovacuum
        FROM pg_stat_user_tables
        ORDER BY dead_rows DESC;
    """
    
    conn = get_db_connection()
    if not conn:
        return []
    
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        tables = cursor.fetchall()
        cursor.close()
        conn.close()
        
        results = []
        for t in tables:
            t_dict = dict(t)
            t_dict['dead_row_percent'] = float(t_dict['dead_row_percent']) if t_dict['dead_row_percent'] else 0.0
            t_dict['last_vacuum'] = str(t_dict['last_vacuum']) if t_dict['last_vacuum'] else None
            t_dict['last_autovacuum'] = str(t_dict['last_autovacuum']) if t_dict['last_autovacuum'] else None
            results.append(t_dict)
            
        return results
    except Exception as e:
        print(f"❌ Tablo analiz hatası: {e}")
        if conn:
            conn.close()
        return []