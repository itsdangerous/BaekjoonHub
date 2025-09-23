from collections import deque

direction = [
    [-1, 0, 0],
    [1, 0, 0],
    [0, 0, 1],
    [0, 0, -1],
    [0, 1, 0],
    [0, -1, 0],
]

M, N, H = map(int, input().split())

def searchable(z, r, c):
    return 0 <= z < H and 0 <= r < N and 0 <= c < M

arr = []
que = deque()
visited = [[[False]*M for i in range(N)] for h in range(H)]
time = -1
targets = 0
for h in range(H):
    arr.append([])
    for i in range(N):
        line = list(map(int, input().split()))
        arr[h].append(line)
        for j in range(M):
            if arr[h][i][j] == 1:
                que.appendleft([h,i,j])
                visited[h][i][j] = True
            elif arr[h][i][j] == 0:
                targets += 1

while que:
    time += 1
    len_que = len(que)
    while len_que > 0:
        len_que -= 1
        cur_z, cur_r, cur_c = que.pop()
        for dz, dr, dc in direction:
            nz, nr, nc = cur_z + dz, cur_r + dr, cur_c + dc
            if not searchable(nz, nr, nc): continue
            if visited[nz][nr][nc]: continue
            if arr[nz][nr][nc] == -1: continue
            if arr[nz][nr][nc] == 1: continue

            visited[nz][nr][nc] = True
            arr[nz][nr][nc] = 1
            que.appendleft([nz, nr, nc])
            targets -= 1
if targets:
    print(-1)
else:
    print(time)
