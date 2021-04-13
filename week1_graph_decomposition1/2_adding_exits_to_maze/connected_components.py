#Uses python3

import sys


def number_of_components(adj_list):
    result = 0
    visited = [False for x in range(len(adj_list))]

    def explore(v):
        visited[v] = True
        for index in adj_list[v]:
            if visited[index] is not True:
                explore(index)

    for item in range(len(adj_list)):
        if not visited[item]:
            explore(item)
            result += 1

    return result


def test(input_data):
    n, m = input_data[0:2]
    data = input_data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    return number_of_components(adj)


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
    print(number_of_components(adj))
