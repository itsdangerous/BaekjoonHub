N, M = map(int, input().split())

arr = sorted(list(map(int, input().split())))

p = [-1] * M
visited = [False] * N
def back_tracking(start, depth: int):
    if depth == M:
        print(*p)
        return

    for d in range(start, N):
        if depth >= 1 and p[depth-1] > arr[d]: continue
        p[depth] = arr[d]
        back_tracking(start, depth+1)

back_tracking(0,0 )