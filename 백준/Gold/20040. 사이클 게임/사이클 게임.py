import sys

input = sys.stdin.readline

N, M = map(int, input().split())

p = [i for i in range(N)]

rank = [1 for _ in range(N)]


def find(x):
    while x != p[x]:
        x = p[x]

    return x


def union(x, y):
    px = find(x)
    py = find(y)

    if px == py:
        return False

    else:
        if rank[px] > rank[py]:
            p[py] = px
        elif rank[py] < rank[px]:
            p[px] = py
        else:
            p[py] = px
            rank[px] += 1
        return True


flag = False
for i in range(M):
    a, b = map(int, input().split())
    if not union(a, b):
        flag = True
        print(i + 1)
        break

if not flag:
    print(0)