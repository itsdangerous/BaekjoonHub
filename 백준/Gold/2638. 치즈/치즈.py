from collections import deque


def check(r: int, c: int) -> bool:
    return 0 <= r < N and 0 <= c < M


def count_cheeses(map: list) -> int:
    count = 0
    for i in map:
        for j in i:
            if j == 1:
                count += 1
    return count


# 공기는 9로 마킹하기
def mark(map: list) -> None:
    visited = [[False for _ in range(M)] for _ in range(N)]
    que = deque()
    que.append([0, 0])
    map[0][0] = 9
    visited[0][0] = True

    while que:
        pos = que.popleft()
        for i in range(4):
            nr = pos[0] + dr[i]
            nc = pos[1] + dc[i]
            if not check(nr, nc):
                continue
            if visited[nr][nc]:
                continue
            if map[nr][nc] == 1:
                continue
            que.append([nr, nc])
            map[nr][nc] = 9
            visited[nr][nc] = True


def melt(map: list, cnt_cheese: int) -> int:
    melted_cheeses = deque()

    for r in range(N):
        for c in range(M):
            if map[r][c] == 1:
                cnt_air = 0
                for k in range(4):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    if not check(nr, nc):
                        continue
                    if map[nr][nc] != 9:
                        continue
                    cnt_air += 1
                    if cnt_air == 2:
                        break
                if cnt_air != 2:
                    continue
                cnt_cheese -= 1
                map[r][c] = 2
                melted_cheeses.append([r, c])

    while melted_cheeses:
        melt_pos = melted_cheeses.popleft()
        map[melt_pos[0]][melt_pos[1]] = 9
    return cnt_cheese


N, M = map(int, input().split())
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

map = [list(map(int, input().split())) for _ in range(N)]
cnt_cheese = count_cheeses(map)

time = 0
while cnt_cheese > 0:
    mark(map)
    # print(cnt_cheese)
    # for i in map:
    #     print(i)
    # print("---------")
    time += 1
    cnt_cheese = melt(map, cnt_cheese)
# for i in map:
#     print(i)
# print("---------")
print(time)