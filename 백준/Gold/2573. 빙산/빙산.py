from collections import deque

N, M = map(int, input().split())
map_data = [list(map(int, input().split())) for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 빙산이 녹는 함수
def melt():
    global map_data, N, M
    melted = [[0] * M for _ in range(N)]
    for r in range(N):
        for c in range(M):
            if map_data[r][c] > 0:
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if 0 <= nr < N and 0 <= nc < M and map_data[nr][nc] == 0:
                        melted[r][c] += 1
    for r in range(N):
        for c in range(M):
            map_data[r][c] = max(map_data[r][c] - melted[r][c], 0)

# 섬의 개수를 확인하는 함수
def check_separation():
    global map_data, N, M, dr, dc
    visited = [[False] * M for _ in range(N)]
    count = 0
    for r in range(N):
        for c in range(M):
            if map_data[r][c] > 0 and not visited[r][c]:
                count += 1
                if count >= 2:
                    return count
                q = deque([(r, c)])
                visited[r][c] = True
                while q:
                    cur_r, cur_c = q.popleft()
                    for i in range(4):
                        nr = cur_r + dr[i]
                        nc = cur_c + dc[i]
                        if 0 <= nr < N and 0 <= nc < M and map_data[nr][nc] > 0 and not visited[nr][nc]:
                            q.append((nr, nc))
                            visited[nr][nc] = True
    return count

# 해결 함수
def solve():
    year = 0
    while True:
        if check_separation() >= 2:
            return year
        if not any(map_data[r][c] for r in range(N) for c in range(M)):
            return 0
        melt()
        year += 1

print(solve())