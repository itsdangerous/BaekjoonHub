# import sys
from collections import deque
# sys.stdin = open("input.txt", "r")

N = int(input())

directions = [
    [-1, 0],
    [0, 1],
    [1, 0],
    [0, -1],
]

def inline(r, c):
    return 0<=r<N and 0<=c<N

arr = []

max_h = 0
for i in range(N):
    arr.append(list(map(int, input().split())))
    for j in range(N):
        max_h = max(max_h, arr[i][j])

max_cnt = 0
# 높이는 2부터 계산할 것
def bfs(h):
    global max_cnt
    cnt = 0
    visited = [[False] * N for _ in range(N)]
    que = deque()
    for i in range(N):
        for j in range(N):
            if visited[i][j]: continue
            if arr[i][j] - h <= 0: continue
            cnt += 1
            que.appendleft([i, j])
            visited[i][j] = True
            while que:
                cur_r, cur_c = que.pop()
                for dr, dc in directions:
                    nr, nc = cur_r + dr, cur_c + dc
                    if not inline(nr ,nc): continue
                    if visited[nr][nc]: continue
                    if arr[nr][nc] -h <= 0: continue
                    que.appendleft([nr, nc])
                    visited[nr][nc] = True
    max_cnt = max(max_cnt, cnt)

for h in range(max_h, -1, -1):
    bfs(h)

print(max_cnt)