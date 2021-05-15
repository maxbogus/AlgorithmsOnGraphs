# Uses python3

import sys
import queue


def BFS(adj_list, S):
    dist = [-1] * len(adj_list)
    prev = [None] * len(adj_list)
    dist[S] = 0
    q = queue.Queue(maxsize=len(adj_list))
    q.put(S)
    while not q.empty():
        u = q.get()
        for node in adj_list[u]:
            if dist[node] == -1:
                q.put(node)
                dist[node] = dist[u] + 1
                prev[node] = u
    return dist


def distance(adj_list, s, t):
    result = BFS(adj_list, s)
    return result[t]


def test(test_data):
    n, m = test_data[0:2]
    test_data = test_data[2:]
    graph_edges = list(zip(test_data[0:(2 * m):2], test_data[1:(2 * m):2]))
    adj_list = [[] for _ in range(n)]
    for (a, b) in graph_edges:
        adj_list[a - 1].append(b - 1)
        adj_list[b - 1].append(a - 1)
    s, t = test_data[2 * m] - 1, test_data[2 * m + 1] - 1
    return distance(adj_list, s, t)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
