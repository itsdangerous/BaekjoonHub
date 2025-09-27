from collections import deque

DIRECTIONS = [
    [-1, 0],
    [0, 1],
    [1, 0],
    [0, -1],
]

def rotate_table(direction, table) -> list:
    global N
    temp_table = [[-1] * N for _ in range(N)]

    if direction == [-1, 0]: temp_table = [row[:] for row in table]

    # 좌회전
    elif direction == [0, -1]:
        for c in range(N-1, -1, -1):
            for r in range(N):
                temp_table[N-1-c][r] = table[r][c]
    # 우회전
    elif direction == [0, 1]:
        for c in range(N):
            for r in range(N-1, -1, -1):
                temp_table[c][N-1-r] = table[r][c]
    # 90도 회전
    elif direction == [1, 0]:
        for r in range(N):
            for c in range(N):
                temp_table[N-1-r][N-1-c] = table[r][c]
    return temp_table

def search(r, c, arr):
    # table[r][c]로부터 위쪽까지 탐색하며, 0이 아닌 값이 나올 때까지 찾고,
    # 이동한 값을 반환한다.
    nr = r
    while 0 <= nr -1:
        nr -= 1
        if arr[nr][c] != 0:
            break
    return [nr, c, r-nr] # 3번째 값은, 탐색을 한번이라도 했는지 판단하기 위해서며, 이 값이 0값을 가지면, 탐색을 하지 않았음을 의미하고 이는 곧 자기 자신을 의미한다.


def update_table(origin_table) -> list:
    table = [row[:] for row in origin_table]
    # rotate가 이미 되었으니, 모든 값을 위로 올리는 작업을 진행한다.

    # 1. 테이블의 모든 값을 순회하며, 위쪽 끝방향으로, 0이 아닌 값이 나올때까지 값을 찾고, 값을 찾았다면, 찾은 값의 position이 visited인지 확인 후, 아니라면 현재 값과 동일하면 visited를 True로 표기한다.
    # 2. visited된 요소의 position을 table에서 찾고 0으로 바꾼 후, 위쪽 방향의 값을 *2한다.
    # 3. 모든 요소를, 위쪽으로 붙인다. 붙이는 과정은, 각 요소가 위쪽을 탐색하며, 0이 아닌 값을 만날때 까지다.

    # visited는 사라질 position에 대해 저장한다.
    visited = [[False] * N for _ in range(N)]
    targets = []

    # 1. 모든 값에 대해, 위쪽 끝까지 탐색하고, visited 처리를 한다.
    for r in range(N):
        for c in range(N):
            if table[r][c] == 0: continue
            get_r, get_c, search_cnt = search(r, c, table)
            if search_cnt == 0: continue # 자기 자신이라면 넘긴다.
            if visited[get_r][get_c]: continue # 찾은 값은, 합쳐질 예정이므로 넘긴다.
            if table[get_r][get_c] != table[r][c]: continue # 값이 같아야지만 합친다.
            visited[r][c] = True # get_r, get_c 대신 r, c에 대한 즉, 사라질 position을 visited 처리해야한다.
            targets.append([get_r, get_c]) # 값을 올릴 (*2) position을 append한다.

    # 2. targets를 순회하며 값을 *2해준 후, visited에 있는 값을 모두 0으로 만든다.
    for r, c in targets:
        table[r][c] = table[r][c] * 2

    for r in range(N):
        for c in range(N):
            if visited[r][c]: table[r][c] = 0

    # 3. search함수를 재활용하여, 이제 모든 값을 위로 붙인다.
    # 찾은 값이 0이라면, 찾은 row값이 0인 경우에만 이동한다.
    # 찾은 값이 0이 아니라면, 찾은 row값 +1과 현재 row 값의 차이가 있는지 확인후, 차이가 있는 경우에만 업데이트한다.
    for r in range(N):
        for c in range(N):
            if table[r][c] == 0: continue
            get_r, get_c, search_cnt = search(r, c, table)
            if search_cnt == 0: continue
            if table[get_r][get_c] == 0:
                if get_r != 0: continue
                table[get_r][get_c] = table[r][c]
                table[r][c] = 0

            else:
                if get_r + 1 == r: continue
                table[get_r + 1][get_c] = table[r][c] # get_r + 1을 해줌으로써 0이 아닌 값 바로 밑에 위치하도록 한다.
                table[r][c] = 0

    return table

N= int(input())
R = 5

table = []
for i in range(N):
    line = list(map(int, input().split()))
    table.append(line)

que = deque()
que.append([table, 0])
max_val = 0
while que:
    cur_table, cnt = que.popleft()
    if cnt > R:
        break
    max_val = max(max_val, max(map(max, cur_table)))

    for direction in DIRECTIONS:
        rotated_table = rotate_table(direction, cur_table)
        updated_table = update_table(rotated_table)
        if updated_table == cur_table: continue
        que.append([updated_table, cnt + 1])
print(max_val)