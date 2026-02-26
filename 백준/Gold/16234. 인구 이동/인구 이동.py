from collections import deque
# 인구 이동은 하루 동안 다음과 같이 진행되고, 더 이상 아래 방법에 의해 인구 이동이 없을 때까지 지속된다.
#
# 국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루 동안 연다.
# 위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작한다.
# 국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안은 연합이라고 한다.
# 연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
# 연합을 해체하고, 모든 국경선을 닫는다.
# 각 나라의 인구수가 주어졌을 때, 인구 이동이 며칠 동안 발생하는지??????????

N, L, R = map(int, input().split())

arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))

directions = [
    [-1, 0],
    [0, 1],
    [1, 0],
    [0, -1],
]

def check(r, c):
    return 0 <= r < N and 0 <= c < N


def get_whole_adj_nations():
    que = deque()
    visited = [[False] * N for _ in range(N)]
    whole_adj_nations = []
    for r in range(N):
        for c in range(N):
            if visited[r][c]: continue
            visited[r][c] = True
            que.append([r, c])
            adj_nations = [(r, c)]
            while que:
                cr, cc = que.popleft()
                for dr, dc in directions:
                    nr, nc = cr + dr, cc + dc
                    if not check(nr, nc): continue
                    if visited[nr][nc]: continue
                    # 국경선 열 수 있는지 체크
                    if L <= abs(arr[cr][cc] - arr[nr][nc]) <= R:
                        visited[nr][nc] = True
                        que.append([nr, nc])
                        adj_nations.append((nr, nc))
            whole_adj_nations.append(adj_nations)

    return whole_adj_nations


cnt = 0
while True:
    whole_adj_nations = get_whole_adj_nations()
    is_movable = False
    for adj_nations in whole_adj_nations:
        if len(adj_nations) < 2: continue
        is_movable = True
        population = 0
        for r, c in adj_nations:
            population += arr[r][c]
        average_population = population // len(adj_nations)
        for r, c in adj_nations:
            arr[r][c] = average_population
    # print(arr)
    # print()
    if not is_movable:
        break
    else:
        cnt += 1

print(cnt)