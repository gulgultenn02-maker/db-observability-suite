from fastapi import FastAPI, Query
from apscheduler.schedulers.background import BackgroundScheduler
from collectors.slow_queries import fetch_slow_queries
from collectors.table_health import fetch_table_bloat_and_stats
from collectors.alert_engine import run_health_checks
from collectors.index_health import fetch_unused_indexes

app = FastAPI(
    title="Enterprise Database Observability Suite",
    description="PostgreSQL performansını, yavaş sorguları ve veritabanı sağlığını izleyen otomasyon servisi.",
    version="1.0.0"
)

scheduler = BackgroundScheduler()

@app.on_event("startup")
def startup_event():
    scheduler.add_job(run_health_checks, 'interval', seconds=30)
    scheduler.start()

@app.on_event("shutdown")
def shutdown_event():
    scheduler.shutdown()

@app.get("/")
def read_root():
    return {
        "status": "online",
        "service": "Database Observability Suite",
        "version": "1.0.0"
    }

@app.get("/api/v1/slow-queries")
def get_slow_queries(threshold: float = Query(default=1.0, description="Kaç saniyeden uzun süren sorgular çekilsin?")):
    queries = fetch_slow_queries(threshold_seconds=threshold)
    return {
        "threshold_seconds": threshold,
        "count": len(queries),
        "data": queries
    }

@app.get("/api/v1/table-health")
def get_table_health():
    table_stats = fetch_table_bloat_and_stats()
    return {
        "total_tables": len(table_stats),
        "data": table_stats
    }

@app.get("/api/v1/unused-indexes")
def get_unused_indexes():
   
    unused = fetch_unused_indexes()
    return {
        "total_unused_indexes": len(unused),
        "data": unused
    }