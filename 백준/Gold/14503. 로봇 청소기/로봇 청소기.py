def movable(r, c):
    return 0 <= r < N and 0 <= c < M


directions = [
    [-1, 0],
    [0, 1],
    [1, 0],
    [0, -1],
]


N, M = map(int, input().split())


cr, cc, cd = map(int, input().split())

arr = []

for i in range(N):
    line = list(map(int, input().split()))
    arr.append(line)

cnt = 0  # 청소 개수


def simulation(r, c, d):
    global cnt

    while True:
        # 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
        if arr[r][c] == 0:
            arr[r][c] = 9
            cnt += 1

        found_not_cleaned = False
        for i in range(4):
            nr, nc = r + directions[i][0], c + directions[i][1]
            if not movable(nr, nc): continue
            if arr[nr][nc] == 0:
                found_not_cleaned = True
        # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
        if not found_not_cleaned:
            nd = (d + 2) % 4
            nr, nc = r + directions[nd][0], c + directions[nd][1]
            # 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
            if movable(nr, nc) and arr[nr][nc] != 1:
                r, c = nr, nc
                continue
            # 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
            else:
                break
        # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
        else:
            # 반시계 방향으로 90도 회전한다.
            d = (d - 1) % 4
            # 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
            nr, nc = r + directions[d][0], c + directions[d][1]
            if movable(r, c) and arr[nr][nc] == 0:
                r, c = nr, nc
            continue
            # 1번으로 돌아간다.


simulation(cr, cc, cd)
print(cnt)