#Uses python3

import sys
import queue

def distance(adj, s, t):
    #write your code here
    return -1


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
