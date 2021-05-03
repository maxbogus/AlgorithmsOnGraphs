# Uses python3

import sys


def dfs(adj_list, v, visited, stack):
    visited[v] = True

    for i in adj_list[v]:
        if visited[i] == False:
            dfs(adj_list, i, visited, stack)

    stack.append(v)


def toposort(adj_list):
    visited = [False] * len(adj_list)
    stack = []

    for i in range(len(adj_list)):
        if visited[i] == False:
            dfs(adj_list, i, visited, stack)

    return stack[::-1]


def test(input_data):
    n, m = input_data[0:2]
    data = input_data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    return toposort(adj)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')
