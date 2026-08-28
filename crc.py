def bellmanFord(V, edges, src):
    dist = [100000000] * V
    dist[src] = 0
    for i in range(V):
        for edge in edges:
            u, v, wt = edge
            if dist[u] != 100000000 and dist[u] + wt < dist[v]:
                if i == V - 1:
                    return [-1]
                dist[v] = dist[u] + wt
    return dist

if __name__ == '__main__':
    V = 5
    edges = [[1, 3, 2], [4, 3, -1], [2, 4, 1], [1, 2, 1], [0, 1, 5]]

    src = 0
    ans = bellmanFord(V, edges, src)
    print(' '.join(map(str, ans)))
