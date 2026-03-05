from flask import Flask, request, jsonify
import mysql.connector
import heapq

app = Flask(__name__)

# ---------------- DATABASE CONNECTION ----------------

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sakshi@123",
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
@app.route("/")
def home():
    return jsonify({
        "message": "Smart Delivery Route Optimization API Running",
        "status": "OK"
    })

# ---------------- API ROUTE ----------------

@app.route("/route", methods=["GET"])
def get_route():

    start = int(request.args.get("start"))
    end = int(request.args.get("end"))

    graph = load_graph()

    path, distance = dijkstra(graph, start, end)

    return jsonify({
        "start_location": start,
        "end_location": end,
        "optimal_route": path,
        "total_distance": distance
    })

# ---------------------DELIVERY ORDER(API) ---------------------
@app.route("/deliveries")
def get_deliveries():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM deliveries")

    rows = cursor.fetchall()

    deliveries = []

    for row in rows:
        deliveries.append({
            "delivery_id": row[0],
            "order_name": row[1],
            "source_location": row[2],
            "destination_location": row[3],
            "status": row[4]
        })

    return jsonify(deliveries)

# ---------------- RUN SERVER ----------------

if __name__ == "__main__":
    app.run(debug=True)