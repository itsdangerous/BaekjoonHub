from collections import deque

direction = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
]

def searchable(r, c):
    global N
    return 0 <= r < N and 0<= c < M

M, N = map(int, input().split())

arr = []
que = deque()
visited = [[False]*M for i in range(N)]
time = -1
targets = 0
for i in range(N):
    line = list(map(int, input().split()))
    arr.append(line)
    for j in range(M):
        if arr[i][j] == 1:
            que.appendleft([i,j])
            visited[i][j] = True
        elif arr[i][j] == 0:
            targets += 1

while que:
    time += 1
    len_que = len(que)
    while len_que > 0:
        len_que -= 1
        cur_r, cur_c = que.pop()
        for dr, dc in direction:
            nr, nc = cur_r + dr, cur_c + dc
            if not searchable(nr, nc): continue
            if visited[nr][nc]: continue
            if arr[nr][nc] == -1: continue
            if arr[nr][nc] == 1: continue

            # arr[nr][nc] == 0
            visited[nr][nc] = True
            arr[nr][nc] = 1
            que.appendleft([nr, nc])
            targets -= 1
if targets:
    print(-1)
else:
    print(time)
