import sys

input = sys.stdin.readline
arr = []
blank = []
arr = [list(map(int, input().split())) for _ in range(9)]
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            blank.append([i, j])
R = len(blank)


def check(num: int, r: int, c: int) -> bool:
    if num in arr[r]:
        return False

    for row in range(9):
        if num == arr[row][c]:
            return False

    start_r = (r // 3) * 3
    start_c = (c // 3) * 3
    for i in range(start_r, start_r + 3):
        for j in range(start_c, start_c + 3):
            if num == arr[i][j]:
                return False
    return True


def dfs(cnt: int):
    if cnt == R:
        return True

    r, c = blank[cnt]
    for i in range(1, 10):
        if check(i, r, c):
            arr[r][c] = i
            result = dfs(cnt + 1)
            if result:
                return True
            arr[r][c] = 0
    return False


dfs(0)
for i in arr:
    print(*i)