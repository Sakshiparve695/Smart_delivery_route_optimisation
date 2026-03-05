# 🚚 Smart Delivery Route Optimization System

A smart logistics optimization system that computes the **shortest delivery route between locations** using graph algorithms. The system models delivery locations as nodes and roads as weighted edges stored in a database.

The optimal delivery path is calculated using **Dijkstra's Shortest Path Algorithm**.

---

# 🚀 Features

- Load road network from database
- Represent delivery locations as a weighted graph
- Compute optimal delivery route between locations
- Calculate total travel distance
- Visualize delivery network using graph visualization
- Highlight the optimal route in the network

---

# 🛠 Tech Stack

- Python
- MySQL
- NetworkX
- Matplotlib

---

# 📊 Algorithm Used

The system uses **Dijkstra's Algorithm** to determine the shortest path between two delivery locations.

Steps:

1. Load road network from database  
2. Build graph representation of locations  
3. Apply Dijkstra's shortest path algorithm  
4. Return the optimal delivery route and total distance  

---

# 📷 Route Optimization Visualization

The delivery network is visualized as a graph where:

- Nodes represent delivery locations
- Edges represent roads between locations
- Edge weights represent distances
- The optimal route is highlighted in the graph

Example output:

```
Optimal Route: [1, 2, 6, 10]
Total Distance: 15
```

---

# 🗂 Project Structure

```
Smart-Delivery-Route-Optimization
│
├── smart_route_delivery.py
├── API_Server.py
├── database.sql
├── README.md
```

---

# ⚙️ How to Run the Project

1. Install required libraries

```
pip install mysql-connector-python
pip install networkx
pip install matplotlib
```

2. Run the program

```
python smart_route_delivery.py
```

---

# 🔮 Future Improvements

- Multi-delivery route optimization
- Web dashboard for route visualization
- Integration with real-time traffic data
- API-based delivery route service

---

# 👩‍💻 Author

**Sakshi Parve**
