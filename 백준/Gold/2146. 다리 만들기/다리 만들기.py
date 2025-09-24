import copy
from collections import deque

directions = [
    [-1, 0],
    [0, 1],
    [1, 0],
    [0, -1],
]

def print_arr(a: list[list]):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end='\t')
        print()

def searchable(r, c):
    global N
    return 0<=r<N and 0<=c<N

def is_aside_sea(r, c):
    global N, arr
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if not searchable(nr, nc): continue
        if arr[nr][nc] == 0:
            return True
    return False



N = int(input())

arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
# print(*arr)
visited = [[False] * N for _ in range(N)]
que = deque()
cnt = -1
points = []
for i in range(N):
    for j in range(N):
        if visited[i][j]: continue
        if arr[i][j] == 0: continue
        que.appendleft([i, j])
        visited[i][j] = True
        cnt += 1
        points.append([])
        # bfs
        while que:
            cur_r, cur_c = que.pop()
            if is_aside_sea(cur_r, cur_c):
                points[cnt].append([cur_r, cur_c])
            for dr, dc in directions:
                nr, nc = cur_r + dr, cur_c + dc
                if not searchable(nr, nc): continue
                if visited[nr][nc]: continue

                # 가장자리인 것들을 각 섬별로 모으기
                if arr[nr][nc] == 0:
                    # arr[cur_r][cur_c] = cnt +1
                    continue
                que.appendleft([nr, nc])
                visited[nr][nc] = True

# print_arr(points)
INF = 10**9
ans = INF

for a in range(len(points)):
    for b in range(a + 1, len(points)):
        for ra, ca in points[a]:
            for rb, cb in points[b]:
                d = abs(ra - rb) + abs(ca - cb) - 1
                if d < ans:
                    ans = d
        # 이쯤에서 ans가 0이면 더 줄 수 없으니 빠르게 종료 가능
        if ans == 0:
            break
    if ans == 0:
        break

print(ans)

