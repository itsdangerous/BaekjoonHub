arr = []

poses = {}

for i in range(5):
    line = list(map(int, input().split()))
    arr.append(line)
    for j in range(5):
        poses[line[j]] = i, j


def rotate_rect():
    rotated_arr = [[0] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            rotated_arr[i][j] = arr[5 - j - 1][i]

    return rotated_arr


def get_lines() -> int:
    cnt_line = 0

    rotated_arr = rotate_rect()

    for i in range(5):
        # 가로
        if sum(arr[i]) == 0: cnt_line += 1
        # 세로
        if sum(rotated_arr[i]) == 0: cnt_line += 1

    sum_cross_1 = 0
    sum_cross_2 = 0
    for i in range(5):
        sum_cross_1 += arr[i][i]
        sum_cross_2 += arr[5 - i - 1][i]

    if sum_cross_1 == 0: cnt_line += 1
    if sum_cross_2 == 0: cnt_line += 1

    return cnt_line


cnt = 0
for i in range(5):
    nums = list(map(int, input().split()))
    for num in nums:
        cnt += 1
        r, c = poses[num]
        arr[r][c] = 0

        if cnt < 12:
            # 최소 12개 이상부터 3개의 빙고가 나올 수 있으므로,
            # 그 이하에서는 빙고 검사하지 않음
            continue
        else:
            cnt_lines = get_lines()
            if cnt_lines >= 3:
                print(cnt)
                exit()
