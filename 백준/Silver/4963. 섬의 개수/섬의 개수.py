from collections import deque

directions = [
    [-1, -1],
    [-1, 0],
    [-1, 1],
    [0, 1],
    [1, 1],
    [1, 0],
    [1, -1],
    [0, -1]
]

def searchable(r, c, n, m):
    return 0 <= r < n and 0 <= c < m

def bfs():
    while True:
        m, n = map(int, input().split())
        if not m and not n: return

        arr = []
        for i in range(n):
            arr.append(list(map(int, input().split())))

        visited = [[False] * m for i in range(n)]
        que = deque()
        cnt = 0
        for i in range(n):
            for j in range(m):
                if visited[i][j]: continue
                if arr[i][j] != 1: continue
                visited[i][j] = True
                que.appendleft([i, j])
                cnt += 1

                # bfs (visited 처리)
                while que:
                    cur_r, cur_c = que.pop()
                    for dr, dc in directions:
                        nr, nc = cur_r + dr, cur_c + dc
                        if not searchable(nr, nc, n, m): continue
                        if visited[nr][nc]: continue
                        if arr[nr][nc] != 1: continue
                        visited[nr][nc] = True
                        que.appendleft([nr, nc])

        print(cnt)
bfs()
