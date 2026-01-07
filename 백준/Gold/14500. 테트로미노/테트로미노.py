def print_arr(a):
    for row in a:
        print(row)


def movable(r, c):
    return 0 <= r < N and 0 <= c < M


directions = [
    [-1, 0],
    [0, 1],
    [1, 0],
    [0, -1],
]

N, M = map(int, input().split())

arr = []
for i in range(N):
    arr.append([])
    line = list(map(int, input().split()))
    arr[i] = line[:]

# print_arr(arr)

# simulate with back-tracking
max_sum = 0
max_val = max(map(max, arr))

def simulate(r, c, cur_cnt, cur_sum):
    global max_sum

    if cur_sum + max_val * (4 - cur_cnt) <= max_sum:
        return

    if cur_cnt == 4:
        max_sum = max(max_sum, cur_sum)
        return

    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if not movable(nr, nc): continue
        if visited[nr][nc]: continue
        visited[nr][nc] = True
        simulate(nr, nc, cur_cnt + 1, cur_sum + arr[r][c])
        visited[nr][nc] = False


def simulate2(r, c):
    global max_sum

    center_val = arr[r][c]

    wings = []
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if movable(nr, nc):
            wings.append(arr[nr][nc])

    if len(wings) < 3:
        return

    if len(wings) == 4:
        wings.sort(reverse=True)
        wings.pop()

    max_sum = max(max_sum, center_val + sum(wings))


visited = [[False] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        # 한붓 그리기
        visited[i][j] = True
        simulate(i, j, 0, 0)
        visited[i][j] = False

        # ㅗ자모양 체크
        simulate2(i, j)
print(max_sum)
