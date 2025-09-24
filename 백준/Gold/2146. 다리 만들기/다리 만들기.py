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
        # bfs
        while que:
            cur_r, cur_c = que.pop()
            if is_aside_sea(cur_r, cur_c):
                points.append([cur_r, cur_c])
            for dr, dc in directions:
                nr, nc = cur_r + dr, cur_c + dc
                if not searchable(nr, nc): continue
                if visited[nr][nc]: continue

                if arr[nr][nc] == 0:
                    arr[cur_r][cur_c] = cnt + 2
                    continue
                que.appendleft([nr, nc])
                visited[nr][nc] = True

# print_arr(arr)

min_d = 200
for r, c in points:
    visited = [[False] * N for _ in range(N)]
    que = deque()
    que.appendleft([r, c])
    visited[r][c] = True
    d = -1
    while que:
        len_que = len(que)
        if d >= min_d: break
        while len_que > 0:
            cur_r, cur_c = que.pop()
            if arr[cur_r][cur_c] != 0 and arr[cur_r][cur_c] != arr[r][c]:
                min_d = min(min_d, d)
                # test_arr = copy.deepcopy(arr)
                # test_arr[r][c] = "*"
                # test_arr[cur_r][cur_c] = "@"
                # print_arr(test_arr)
                # print(f"d: {min_d}")
                break
            len_que -= 1

            for dr, dc in directions:
                nr, nc = cur_r + dr, cur_c + dc
                if not searchable(nr ,nc): continue
                if visited[nr][nc]: continue
                if arr[nr][nc] == 1: continue
                que.appendleft([nr, nc])
                visited[nr][nc] = True

        d += 1

print(min_d)


