from database import get_db_connection

def fetch_slow_queries(threshold_seconds=1):
    
    query = """
        SELECT 
            pid,
            usename AS user_name,
            client_addr AS client_ip,
            now() - query_start AS duration,
            state,
            query
        FROM pg_stat_activity
        WHERE state != 'idle'
          AND (now() - query_start) > INTERVAL '%s second'
          AND pid != pg_backend_pid()
        ORDER BY duration DESC;
    """
    
    conn = get_db_connection()
    if not conn:
        return []
    
    try:
        cursor = conn.cursor()
        cursor.execute(query % threshold_seconds)
        slow_queries = cursor.fetchall()
        cursor.close()
        conn.close()
        
        
        results = []
        for q in slow_queries:
            q_dict = dict(q)
            q_dict['duration'] = str(q_dict['duration'])
            results.append(q_dict)
            
        return results
    except Exception as e:
        print(f"❌ Yavaş sorgu analizi hatası: {e}")
        if conn:
            conn.close()
        return []