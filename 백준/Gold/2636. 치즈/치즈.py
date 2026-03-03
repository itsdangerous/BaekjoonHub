from collections import deque


def check(r, c):
    return 0 <= r < H and 0 <= c < W


directions = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
]

H, W = map(int, input().split())

arr = []
sum_cheese = 0
for i in range(H):
    line = list(map(int, input().split()))
    sum_cheese += sum(line)
    arr.append(line)


def mark_side_cheese_for_bfs():
    count_side_cheese = []
    que = deque()
    visited = [[False] * W for _ in range(H)]
    que.append([0, 0])
    visited[0][0] = True

    while que:
        cur_r, cur_c = que.popleft()
        for dr, dc in directions:
            nr, nc = cur_r + dr, cur_c + dc
            if not check(nr, nc): continue
            if visited[nr][nc]: continue
            if arr[nr][nc] == 1:
                arr[nr][nc] = 9
                count_side_cheese.append([nr, nc])

                continue
            if arr[nr][nc] == 0:
                visited[nr][nc] = True
                que.append([nr, nc])
    return count_side_cheese


def remove_side_cheese(side_cheese_arr):
    global arr

    for r, c in side_cheese_arr:
        arr[r][c] = 0

    return None


if sum_cheese == 0:
    print(0)
    print(0)

else:
    memory = [sum_cheese]
    cnt = 0
    while sum_cheese:
        cnt += 1
        side_cheese = mark_side_cheese_for_bfs()
        remove_side_cheese(side_cheese)
        sum_cheese -= len(side_cheese)
        memory.append(sum_cheese)

    print(cnt)
    print(memory[-2])
