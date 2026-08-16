#include <iostream>
#include <vector>
#include <queue>
#include <climits>
using namespace std;

// Pair: {distance, vertex}
using pii = pair<int, int>;

void dijkstra(int source, int V, vector<vector<pii>>& graph) {

    // Initialize distances as infinity
    vector<int> dist(V, INT_MAX);

    // Min-priority queue
    priority_queue<pii, vector<pii>, greater<pii>> pq;

    // Distance from source to itself is 0
    dist[source] = 0;
    pq.push({0, source});

    while (!pq.empty()) {

        int currentDist = pq.top().first;
        int u = pq.top().second;
        pq.pop();

        // Ignore outdated entries
        if (currentDist > dist[u])
            continue;

        // Check all adjacent vertices
        for (auto edge : graph[u]) {

            int v = edge.first;
            int weight = edge.second;

            // Relaxation
            if (dist[u] + weight < dist[v]) {
                dist[v] = dist[u] + weight;
                pq.push({dist[v], v});
            }
        }
    }

    // Print shortest distances
    cout << "Shortest distances from vertex " << source << ":\n";

    for (int i = 0; i < V; i++) {
        if (dist[i] == INT_MAX)
            cout << "Vertex " << i << " : INF\n";
        else
            cout << "Vertex " << i << " : " << dist[i] << "\n";
    }
}

int main() {

    int V = 5;

    vector<vector<pii>> graph(V);

    // Add edges: graph[u].push_back({v, weight})

    graph[0].push_back({1, 10});
    graph[0].push_back({4, 5});

    graph[1].push_back({2, 1});
    graph[1].push_back({4, 2});

    graph[2].push_back({3, 4});

    graph[3].push_back({2, 6});
    graph[3].push_back({0, 7});

    graph[4].push_back({1, 3});
    graph[4].push_back({2, 9});
    graph[4].push_back({3, 2});

    // Source vertex = 0
    dijkstra(0, V, graph);

    return 0;
}
