def check(num: int, r: int, c: int, arr: list) -> bool:
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


def solve(arr):
    for r in range(9):
        for c in range(9):
            if arr[r][c] == 0:
                for i in range(1, 10):
                    if check(i, r, c, arr):
                        arr[r][c] = i
                        if solve(arr):
                            return True
                    arr[r][c] = 0
                return False
    return True


arr = [list(map(int, input().split())) for _ in range(9)]
solve(arr)

for row in arr:
    print(" ".join(map(str, row)))