Database Schema and Connection

import psycopg2
from config import DATABASE

def save_daily_summary(summary):
    conn = psycopg2.connect(**DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO daily_summaries (city, avg_temp, max_temp, min_temp, dominant_condition)
        VALUES (%s, %s, %s, %s, %s)
    """, (summary['city'], summary['avg_temp'], summary['max_temp'], summary['min_temp'], summary['dominant_condition']))
    conn.commit()
    cursor.close()
    conn.close()
