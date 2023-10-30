import sys

input = sys.stdin.readline

n, m = map(int, input().split())

p = [i for i in range(n + 1)]  # tree root


def find(x: int):
    global p

    if p[x] == x:
        return x
    else:
        p[x] = find(p[x])
        return p[x]


def union(x: int, y: int):
    global p
    px = find(x)
    py = find(y)

    p[py] = px

    return


def is_union(x: int, y: int):
    px = find(x)
    py = find(y)
    if px == py:
        return True
    return False


def cmd(c: int, a: int, b: int):
    if c == 0:  # union
        union(a, b)
        return

    elif c == 1:  # check
        print("YES") if is_union(a, b) else print("NO")


def solve():
    for i in range(m):
        c, a, b = map(int, input().split())
        cmd(c, a, b)


solve()