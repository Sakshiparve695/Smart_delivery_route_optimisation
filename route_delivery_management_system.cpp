#include <iostream>
#include <unordered_map>
#include <vector>
#include <queue>
#include <limits>
using namespace std;

class RouteSystem {
private:
    unordered_map<string, vector<pair<string, int>>> graph;
    queue<string> deliveryQueue;

public:
    // Add Location
    void addLocation(string loc) {
        if (graph.find(loc) == graph.end()) {
            graph[loc] = {};
            cout << "Location '" << loc << "' added.\n";
        } else {
            cout << "Location already exists.\n";
        }
    }

    // Add Road (edge)
    void addRoad(string src, string dest, int dist) {
        graph[src].push_back({dest, dist});
        graph[dest].push_back({src, dist});
        cout << "Road added between " << src << " and " << dest << " distance " << dist << " km\n";
    }

    // Dijkstra shortest path
    void shortestPath(string start, string end) {
        unordered_map<string, int> distance;
        unordered_map<string, string> parent;

        for (auto &node : graph) {
            distance[node.first] = INT_MAX;
        }

        priority_queue<pair<int, string>, vector<pair<int, string>>, greater<>> pq;

        distance[start] = 0;
        pq.push({0, start});

        while (!pq.empty()) {
            auto [dist, node] = pq.top();
            pq.pop();

            for (auto &neighbor : graph[node]) {
                string next = neighbor.first;
                int weight = neighbor.second;

                if (dist + weight < distance[next]) {
                    distance[next] = dist + weight;
                    parent[next] = node;
                    pq.push({distance[next], next});
                }
            }
        }

        // print path
        cout << "\nShortest Path: ";
        string curr = end;
        vector<string> path;

        while (curr != start) {
            path.push_back(curr);
            curr = parent[curr];
        }
        path.push_back(start);

        for (int i = path.size() - 1; i >= 0; i--) {
            cout << path[i];
            if (i != 0) cout << " -> ";
        }

        cout << "\nTotal Distance: " << distance[end] << " km\n";
    }

    // Add Delivery Order
    void addDelivery(string order) {
        deliveryQueue.push(order);
        cout << "Order '" << order << "' added to queue.\n";
    }

    // Process Delivery
    void processDelivery() {
        if (!deliveryQueue.empty()) {
            cout << "Delivering: " << deliveryQueue.front() << endl;
            deliveryQueue.pop();
        } else {
            cout << "No pending deliveries.\n";
        }
    }

    // View Queue
    void viewQueue() {
        queue<string> temp = deliveryQueue;

        if (temp.empty()) {
            cout << "No pending deliveries.\n";
            return;
        }

        cout << "\nPending Deliveries:\n";
        while (!temp.empty()) {
            cout << "- " << temp.front() << endl;
            temp.pop();
        }
    }
};

int main() {
    RouteSystem system;
    int choice;

    while (true) {
        cout << "\n====== SMART ROUTE SYSTEM (C++) ======\n";
        cout << "1. Add Location\n";
        cout << "2. Add Road\n";
        cout << "3. Find Shortest Route\n";
        cout << "4. Add Delivery Order\n";
        cout << "5. Process Delivery\n";
        cout << "6. View Delivery Queue\n";
        cout << "7. Exit\n";

        cout << "Enter choice: ";
        cin >> choice;
        cin.ignore();

        if (choice == 1) {
            string loc;
            cout << "Enter location: ";
            getline(cin, loc);
            system.addLocation(loc);

        } else if (choice == 2) {
            string src, dest;
            int dist;
            cout << "Enter source: ";
            getline(cin, src);
            cout << "Enter destination: ";
            getline(cin, dest);
            cout << "Enter distance: ";
            cin >> dist;
            cin.ignore();
            system.addRoad(src, dest, dist);

        } else if (choice == 3) {
            string s, d;
            cout << "Enter start: ";
            getline(cin, s);
            cout << "Enter end: ";
            getline(cin, d);
            system.shortestPath(s, d);

        } else if (choice == 4) {
            string order;
            cout << "Enter order: ";
            getline(cin, order);
            system.addDelivery(order);

        } else if (choice == 5) {
            system.processDelivery();

        } else if (choice == 6) {
            system.viewQueue();

        } else if (choice == 7) {
            cout << "Exiting...\n";
            break;

        } else {
            cout << "Invalid choice.\n";
        }
    }

    return 0;
}