import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N = int(input())

arr = [[] for i in range(N+1)]
for i in range(N-1):
    line = list(map(int, input().split()))
    v1, v2 = line
    arr[v1].append(v2)
    arr[v2].append(v1)

parents = [0] * (N+1)
def dfs(parent, cur):
    global arr, parents

    parents[cur] = parent
    for v in arr[cur]:
        if parents[v] != 0:
            continue
        dfs(cur, v)

dfs(0, 1)
for i in range(N+1):
    if i>1:
        print(parents[i])
