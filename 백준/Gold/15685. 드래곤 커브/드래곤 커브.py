N = int(input())

arr = [[False] * 101 for _ in range(101)]

DIR = [
    [0, 1],
    [-1, 0],
    [0, -1],
    [1, 0],
]


def draw_arr(x, y, d, g):
    global arr

    # 방향 리스트 구하기
    cur_g = 0
    directions = [d]
    while cur_g < g:
        cur_g += 1
        next_directions = directions[::-1]
        for i in range(len(next_directions)):
            next_directions[i] = (next_directions[i] + 1) % 4
        directions = directions + next_directions

    # 좌표 표기하기
    nx, ny = x, y
    arr[ny][nx] = True
    for i in directions:
        ny, nx = ny + DIR[i][0], nx + DIR[i][1]
        arr[ny][nx] = True


for n in range(N):
    x, y, d, g = map(int, input().split())
    draw_arr(x, y, d, g)


def check(r, c):
    return 0 <= r < 100 and 0 <= c < 100


result = 0
for r in range(101):
    for c in range(101):
        if not check(r, c): continue
        if not arr[r][c]: continue
        # 현재 점
        # 우
        if not arr[r][c+1]: continue
        # 하
        if not arr[r+1][c]: continue
        # 우측아래대각선
        if not arr[r+1][c+1]: continue
        result += 1

print(result)