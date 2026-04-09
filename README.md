# 🚀 Smart Delivery Intelligence & Optimization Platform

## 📌 Overview

The **Smart Delivery Intelligence Platform** is a cloud-ready backend system designed to optimize delivery routes and provide data-driven insights for logistics operations.

It combines:

* Graph algorithms (Dijkstra) for route optimization
* ETL pipelines for data transformation
* Data warehousing for analytics
* REST APIs for real-time access
* Decision engine for delay prediction and agent recommendation

---

## 🎯 Problem Statement

Traditional delivery systems:

* Do not optimize routes dynamically
* Lack data-driven insights
* Cannot predict delays or evaluate performance

👉 This project solves these issues by building a **scalable backend system with intelligence capabilities**.

---

## 🧠 Key Features

### 🔹 Route Optimization

* Implemented **Dijkstra Algorithm** to compute shortest paths
* Supports traffic-aware cost calculation

### 🔹 Delivery Management APIs

* Create, update, and track deliveries
* RESTful API design using Flask

### 🔹 ETL Pipeline

* Extracts delivery data
* Transforms it into analytics-ready format
* Loads into a **data warehouse (`fact_deliveries`)**

### 🔹 Data Warehouse

* Stores processed delivery metrics
* Enables efficient analytics queries

### 🔹 Analytics APIs

* Top performing agents
* Delivery delay analysis
* Average delivery time

### 🔹 Decision Engine

* Predicts delivery delays
* Recommends best delivery agent

### 🔹 Cloud Deployment

* Backend deployed on cloud platform
* Ready for scalable usage

---

## 🏗️ System Architecture

```
Client → REST API (Flask)
        ↓
   Business Logic Layer
        ↓
   MySQL Database (OLTP)
        ↓
   ETL Pipeline (Python)
        ↓
   Data Warehouse (fact_deliveries)
        ↓
   Analytics & Prediction APIs
```

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **Database:** MySQL
* **Data Processing:** SQL, ETL (Python)
* **Algorithms:** Dijkstra (Graph Theory)
* **Cloud:** Render (API Deployment), Railway (DB - optional)
* **Tools:** Git, GitHub

---

## 📂 Project Structure

```
├── api.py                # Main API server
├── smart_route.py       # Dijkstra algorithm implementation
├── etl.py               # ETL pipeline script
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```
git clone https://github.com/your-username/smart-delivery-api.git
cd smart-delivery-api
```

---

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Configure Database

Update DB connection in `api.py` and `etl.py`:

```python
mysql.connector.connect(
    host="your_host",
    user="your_user",
    password="your_password",
    database="your_db",
    port=3306
)
```

---

### 4️⃣ Run ETL Pipeline

```
python etl.py
```

---

### 5️⃣ Run API Server

```
python api.py
```

---

## 🌐 API Endpoints

### 🔹 Health Check

```
GET /
```

---

### 🔹 Analytics

#### Top Agents

```
GET /analytics/top-agents
```

#### Delay Report

```
GET /analytics/delay-report
```

#### Average Delivery Time

```
GET /analytics/avg-time
```

---

### 🔹 Decision APIs

#### Predict Delay

```
POST /predict-delay
```

**Request Body:**

```json
{
  "agent_id": 1,
  "distance": 10
}
```

---

#### Recommend Agent

```
GET /recommend-agent
```

---

## 📊 Sample Output

```json
[
  {
    "agent_id": 2,
    "avg_time": 17.0
  }
]
```

---

## 🧠 Key Learnings

* Built a **data-driven backend system**
* Implemented **graph algorithms in real-world use case**
* Designed **ETL pipelines and data warehouse**
* Developed **analytics and decision APIs**
* Understood **cloud deployment concepts**

---

## 🚀 Future Enhancements

* Integrate real-time traffic APIs
* Add ML-based delay prediction
* Use AWS S3 for storage
* Deploy fully on AWS (EC2 + RDS)
* Add frontend dashboard

---

## 👩‍💻 Author

**Sakshi Parve**

* Passionate about backend engineering & data systems
* Interested in scalable system design and cloud technologies

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
