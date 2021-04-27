# Uses python3

import sys


def acyclic(adj):
    visited = [False] * len(adj)
    rec_stack = [False] * len(adj)

    def is_cyclic(v):
        visited[v] = True
        rec_stack[v] = True

        for neighbour in adj[v]:
            if not visited[neighbour]:
                if is_cyclic(neighbour):
                    return True
            elif rec_stack[neighbour]:
                return True
        rec_stack[v] = False
        return False

    for node in range(len(adj)):
        if not visited[node]:
            if is_cyclic(node):
                return 1
    return 0


def test(input_data):
    n, m = input_data[0:2]
    data = input_data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    return acyclic(adj)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
