gears = []


def turn(n, d):
    global gears
    global visited

    visited[n] = True
    gear = gears[n]
    top, left, right = gear[0], gear[6], gear[2]

    if d == 1:
        # 시계방향 회전
        gear = gear[-1] + gear[:-1]

    else:  # d == -1
        # 반시계방향 회전
        gear = gear[1:] + gear[0]

    gears[n] = gear

    # 좌, 우 톱니 회전
    if n-1 >= 0 and not visited[n-1]:
        left_gear = gears[n-1]
        left_gear_right_val = left_gear[2]
        if left_gear_right_val != left:
            turn(n-1, -d)

    if n + 1 < 4 and not visited[n+1]:
        right_gear = gears[n+1]
        right_gear_left_val = right_gear[6]
        if right_gear_left_val != right:
            turn(n+1, -d)



for i in range(4):
    line = input()
    gears.append(line)

K = int(input())

for k in range(K):
    n, d = map(int, input().split())
    # n = 번호
    # d = 방향
    # 1: 시계방향
    # -1: 반시계 방향
    visited = [False] * 4
    turn(n-1, d)

sum_top_val = 0
for index, gear in enumerate(gears):
    sum_top_val += int(gear[0]) * 2**index


print(sum_top_val)