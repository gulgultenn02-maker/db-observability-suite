import psycopg2
from psycopg2.extras import RealDictCursor

DB_PARAMS = {
    "dbname": "postgres",
    "user": "rose",        
    "host": "localhost",
    "port": "5432"
}

def get_db_connection():
    try:
        conn = psycopg2.connect(**DB_PARAMS, cursor_factory=RealDictCursor)
        return conn
    except Exception as e:
        print(f"❌ Veritabanı bağlantı hatası: {e}")
        return None