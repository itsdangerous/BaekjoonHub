import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, R, Q = map(int, input().split())
tree = [[] for _ in range(N + 1)]
subtree_size = [0 for i in range(N + 1)]


def dfs(node):
    subtree_size[node] = 1
    for next_node in tree[node]:
        if subtree_size[next_node] != 0:
            continue
        dfs(next_node)
        subtree_size[node] += subtree_size[next_node]


for i in range(N - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

dfs(R)
for i in range(Q):
    q = int(input())
    sys.stdout.write(str(subtree_size[q]) + "\n")
