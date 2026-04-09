import mysql.connector
from datetime import datetime

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sakshi@123",   # (later we can hide this)
        database="smart_delivery_system"
    )

def run_etl():
    conn = connect_db()
    cursor = conn.cursor()

    # Extract data
    cursor.execute("""
        SELECT delivery_id, agent_id, order_time, delivery_time, distance
        FROM deliveries
        WHERE delivery_time IS NOT NULL
    """)

    rows = cursor.fetchall()

    for row in rows:
        delivery_id, agent_id, order_time, delivery_time, distance = row

        # Transform
        duration = int((delivery_time - order_time).total_seconds() / 60)
        is_delayed = duration > 30  # delay rule

        delivery_date = delivery_time.date()

        # Load into warehouse
        cursor.execute("""
            INSERT INTO fact_deliveries (agent_id, delivery_duration, distance, is_delayed, delivery_date)
            VALUES (%s, %s, %s, %s, %s)
        """, (agent_id, duration, distance, is_delayed, delivery_date))

    conn.commit()
    conn.close()
    print("ETL completed successfully")

if __name__ == "__main__":
    run_etl()
    