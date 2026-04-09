from flask import Flask, request, jsonify
import mysql.connector
import heapq
import os
app = Flask(__name__)

# ---------------- DATABASE CONNECTION ----------------

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sakshi@123",   # (later we can hide this)
        database="smart_delivery_system"
    )

# ---------------- LOAD GRAPH FROM DATABASE ----------------

def load_graph():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT source_location, destination_location, distance, traffic_level FROM roads")

    graph = {}

    for src, dest, dist, traffic in cursor.fetchall():
        cost = dist + (traffic * 2)

        graph.setdefault(src, []).append((dest, cost))
        graph.setdefault(dest, []).append((src, cost))

    conn.close()
    return graph

# ---------------- DIJKSTRA ALGORITHM ----------------

def dijkstra(graph, start, end):

    pq = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    parent = {}

    while pq:
        current_distance, node = heapq.heappop(pq)

        if node == end:
            break

        for neighbor, weight in graph[node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                parent[neighbor] = node
                heapq.heappush(pq, (distance, neighbor))

    path = []
    current = end

    while current in parent:
        path.append(current)
        current = parent[current]

    path.append(start)
    path.reverse()

    return path, distances[end]

# --------------- HEALTH CHECK ---------------

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Smart Delivery API Running",
        "status": "OK"
    })

# ---------------- OPTIMIZE ROUTE (UPDATED) ----------------

@app.route("/optimize-route", methods=["POST"])
def optimize_route():

    data = request.get_json()

    if not data:
        return jsonify({"error": "No input provided"}), 400

    start = data.get("start")
    end = data.get("end")

    if start is None or end is None:
        return jsonify({"error": "start and end required"}), 400

    try:
        graph = load_graph()
        path, distance = dijkstra(graph, int(start), int(end))

        return jsonify({
            "optimal_route": path,
            "total_distance": distance
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---------------- ADD DELIVERY (NEW) ----------------

@app.route("/add-delivery", methods=["POST"])
def add_delivery():

    data = request.get_json()

    if not data:
        return jsonify({"error": "No input provided"}), 400

    order_name = data.get("order_name")
    source = data.get("source")
    destination = data.get("destination")

    if not order_name or not source or not destination:
        return jsonify({"error": "Missing fields"}), 400

    try:
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO deliveries (order_name, source_location, destination_location, status) VALUES (%s, %s, %s, %s)",
            (order_name, source, destination, "pending")
        )

        conn.commit()
        conn.close()

        return jsonify({"message": "Delivery added successfully"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---------------- GET DELIVERIES ----------------

@app.route("/deliveries", methods=["GET"])
def get_deliveries():

    try:
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM deliveries")
        rows = cursor.fetchall()

        deliveries = [
            {
                "delivery_id": row[0],
                "order_name": row[1],
                "source_location": row[2],
                "destination_location": row[3],
                "status": row[4]
            }
            for row in rows
        ]

        conn.close()
        return jsonify(deliveries)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
# --------------- COMPLETED ----------------
@app.route("/update-status", methods=["POST"])
def update_status():

    data = request.get_json()

    delivery_id = data.get("delivery_id")
    status = data.get("status")

    if not delivery_id or not status:
        return jsonify({"error": "Missing fields"}), 400

    try:
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE deliveries SET status = %s WHERE delivery_id = %s",
            (status, delivery_id)
        )

        conn.commit()
        conn.close()

        return jsonify({"message": "Status updated successfully"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/predict-delay", methods=["POST"])
def predict_delay():

    data = request.get_json()

    agent_id = data.get("agent_id")
    distance = data.get("distance")

    if not agent_id or not distance:
        return jsonify({"error": "Missing fields"}), 400

    conn = connect_db()
    cursor = conn.cursor()

    # Get agent average delivery time
    cursor.execute("""
        SELECT AVG(delivery_duration)
        FROM fact_deliveries
        WHERE agent_id = %s
    """, (agent_id,))

    result = cursor.fetchone()
    avg_time = result[0] if result[0] else 0

    # Rule-based prediction
    if avg_time > 30 or distance > 8:
        prediction = "Delayed"
    else:
        prediction = "On Time"

    conn.close()

    return jsonify({
        "agent_avg_time": float(avg_time),
        "distance": distance,
        "prediction": prediction
    })

@app.route("/analytics/top-agents", methods=["GET"])
def top_agents():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT agent_id, AVG(delivery_duration) AS avg_time
        FROM fact_deliveries
        GROUP BY agent_id
        ORDER BY avg_time ASC
        LIMIT 5
    """)

    data = cursor.fetchall()

    result = [{"agent_id": row[0], "avg_time": float(row[1])} for row in data]

    conn.close()
    return jsonify(result)

@app.route("/analytics/delay-report", methods=["GET"])
def delay_report():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*), SUM(is_delayed)
        FROM fact_deliveries
    """)

    total, delayed = cursor.fetchone()
    percentage = (delayed / total) * 100 if total > 0 else 0

    conn.close()

    return jsonify({
        "total_deliveries": total,
        "delayed_deliveries": delayed,
        "delay_percentage": round(percentage, 2)
    })

@app.route("/recommend-agent", methods=["GET"])
def recommend_agent():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT agent_id, AVG(delivery_duration) AS avg_time
        FROM fact_deliveries
        GROUP BY agent_id
        ORDER BY avg_time ASC
        LIMIT 1
    """)

    row = cursor.fetchone()

    conn.close()

    return jsonify({
        "recommended_agent": row[0],
        "avg_delivery_time": float(row[1])
    })

# ---------------- RUN SERVER ----------------

if __name__ == "__main__":
    app.run(debug=True)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
