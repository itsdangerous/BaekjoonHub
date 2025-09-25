# import sys
from collections import deque
# sys.stdin = open("input.txt", "r")

directions = [
    [-1, 0],
    [0, 1],
    [1, 0],
    [0, -1],
]

def print_arr(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end=' ')
        print()

def inline(r, c):
    global R, C
    return 0<=r<R and 0<=c<C

R, C, T = map(int, input().split())

arr = []
machine = []
dusts = []
for i in range(R):
    arr.append(list(map(int, input().split())))
    for j in range(C):
        if arr[i][j] == -1:
            machine.append([i, j])
        elif arr[i][j] != 0:
            dusts.append([i, j, arr[i][j]])

def spread(r, c, m):
    global arr
    # r,c 는 좌표, m은 양

    spreadable = []
    # 1. 확산되는 개수 구하고 좌표 구하기
    cnt = 0
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if not inline(nr ,nc):
            continue
        if arr[nr][nc] == -1:
            continue
        spreadable.append([nr, nc])
        cnt += 1

    # 2. 현재 양을 기준으로 확산되는 양 구하기
    spread_v = m//5

    # 4. 확산하기
    arr[r][c] = arr[r][c] - spread_v*cnt
    for tr, tc in spreadable:
        arr[tr][tc] += spread_v



# mode: 1, 2. (1은 위, 2는 아래)
# d: 1,2,3,4 (상우하좌)
def move():
    global arr, machine, R, C
    top_r, top_c = machine[0][0], machine[0][1]
    bottom_r, bottom_c = machine[1][0], machine[1][1]

    # 위쪽: 아래로 밀기 > 좌측으로 밀기 > 위로 밀기 > 우측으로 밀기
    # 아래쪽: 위로 밀기 > 좌측으로 밀기 > 아래로 밀기 > 우측으로 밀기

    # 위쪽
    # 아래로밀기
    for r in range(top_r-1, 0, -1):
        arr[r][0] = arr[r-1][0]
    # 좌측으로 밀기
    for c in range(0, C-1):
        arr[0][c] = arr[0][c+1]
    # 위로 밀기
    for r in range(0, top_r, 1):
        arr[r][C-1] = arr[r+1][C-1]
    # 우측으로 밀기
    for c in range(C-1, top_c, -1):
        arr[top_r][c] = arr[top_r][c-1]
    arr[top_r][top_c+1] = 0

    # 아래쪽
    # 위로 밀기
    for r in range(bottom_r+ 1, R-1):
        arr[r][0] = arr[r+1][0]
    # 좌측으로 밀기
    for c in range(0, C-1):
        arr[R-1][c] = arr[R-1][c+1]
    # 아래로 밀기
    for r in range(R-1, bottom_r, -1):
        arr[r][C-1] = arr[r-1][C-1]
    # 우측으로 밀기
    for c in range(C-1, bottom_c, -1):
        arr[bottom_r][c] = arr[bottom_r][c-1]
    arr[bottom_r][bottom_c+1] = 0
    # print_arr(arr)
    # print()

for t in range(T):
    # 1. 확산
    que = deque(dusts)
    while que:
        cur_r, cur_c, cur_m = que.pop()
        spread(cur_r, cur_c, cur_m)
    # 2. 이동
    cnt = 0
    move()

    # 확산, 이동 후 dusts 구하기
    dusts = []
    for i in range(R):
        for j in range(C):
            if arr[i][j] == -1:
                continue
            if arr[i][j] != 0:
                dusts.append([i, j, arr[i][j]])

result_amount = 0
for i in range(R):
    for j in range(C):
        if arr[i][j] > 0:
            result_amount += arr[i][j]

print(result_amount)
