from collections import deque


def check(r, c):
    return 0 <= r < N and 0 <= c < M


directions = [
    [-1, 0],
    [0, 1],
    [1, 0],
    [0, -1],
]

N, M = map(int, input().split())

arr = []
sum_cheese = 0
for i in range(N):
    line = list(map(int, input().split()))
    arr.append(line)
    sum_cheese += sum(line)


def mark_air_to_nine():
    que = deque()
    visited = [[False] * M for _ in range(N)]
    que.append([0, 0])
    visited[0][0] = True
    arr[0][0] = 9
    while que:
        cr, cc = que.popleft()
        for dr, dc in directions:
            nr, nc = cr + dr, cc + dc
            if not check(nr, nc): continue
            if visited[nr][nc]: continue
            if arr[nr][nc] != 0 and arr[nr][nc] != 9: continue
            arr[nr][nc] = 9
            visited[nr][nc] = True
            que.append([nr, nc])


def remove_cheese():
    removed_cheese = []
    cnt_removed_cheese = 0
    for r in range(N):
        for c in range(M):
            if arr[r][c] != 1: continue
            sum_air = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not check(nr, nc): continue
                if arr[nr][nc] == 9: sum_air += 1
                if sum_air >= 2: break

            if sum_air >= 2:
                removed_cheese.append([r, c])
                cnt_removed_cheese += 1

    for r, c in removed_cheese:
        arr[r][c] = 9

    return cnt_removed_cheese, removed_cheese



cnt = 0
while sum_cheese > 0:
    # for i in arr:
    #     print(i)
    # print()
    # 외부 공기를 9로 마킹
    mark_air_to_nine()
    # for i in arr:
    #     print(i)
    # print()
    # 2개 이상 외부 공기(9)가 인접한 치즈 찾아서 제거 및 제거된 치즈 개수만큼 전체 치즈 개수 업데이트
    cnt_removed_cheese, removed_cheese = remove_cheese()
    # print(removed_cheese)
    sum_cheese -= cnt_removed_cheese
    # for i in arr:
    #     print(i)
    # print()
    # 시간 증가
    cnt += 1

print(cnt)