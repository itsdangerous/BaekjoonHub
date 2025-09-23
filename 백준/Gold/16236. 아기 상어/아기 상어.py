from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

DIRECTION = [
    [-1, 0], # 상
    [0, -1], # 좌
    [0, 1], # 우
    [1, 0], # 하
]
class Shark:
    def __init__(self, t):
        self.remain_capacity = 2
        self.size = 2
        self.position = (-1, -1)
        self.table = t
        self.time = 0

    def print_table(self):
        for i in self.table:
            print(i)

    def eat(self, pos_r, pos_c, d):
        self.table[self.position[0]][self.position[1]] = 0
        self.position = (pos_r, pos_c)
        self.table[pos_r][pos_c] = 9
        self.remain_capacity -= 1
        self.time += d
        if self.remain_capacity == 0:
            self.size += 1
            self.remain_capacity = self.size

    def search_fish(self) -> list:
        # bfs
        que = deque()
        visited = [[False] * len(self.table) for _ in range(len(self.table))]
        que.appendleft(self.position)
        distance = -1
        eatable_candidates = []
        while len(que) > 0:
            distance += 1
            for _ in range(len(que)):
                cur_r, cur_c = que.pop()
                visited[cur_r][cur_c] = True
                if self.table[cur_r][cur_c] != 9 and 0 < self.table[cur_r][cur_c] < self.size:
                    eatable_candidates.append((cur_r, cur_c, distance))
                    # self.eat(cur_r, cur_c, distance)
                    continue
                for dr, dc in DIRECTION:
                    new_r, new_c = cur_r + dr, cur_c + dc
                    if not (0 <= new_r < len(self.table) and 0 <= new_c < len(self.table)): continue
                    if visited[new_r][new_c]: continue
                    if self.table[new_r][new_c] > self.size: continue # 자기 자신보다 큰 경우에는 이동 경로에 포함하지 않음
                    if self.table[new_r][new_c] == 9: continue
                    visited[new_r][new_c] = True
                    # if self.time == 10:
                    #     print(1)
                    que.appendleft((new_r, new_c))
            if eatable_candidates:
                return eatable_candidates
        return eatable_candidates


N = int(input())

table = []
shark = Shark(table)
for i in range(N):
    line = list(map(int, input().split()))
    table.append(line)
    for j in range(N):
        if table[i][j] == 9:
            shark.position = (i, j)

while True:
    candidates = shark.search_fish()
    if not candidates:
        break
    cur_fish_position = candidates[0]
    for candidate in candidates:
        # check priority
        if cur_fish_position[0] > candidate[0]:
            cur_fish_position = candidate
        elif cur_fish_position[0] == candidate[0] and cur_fish_position[1] > candidate[1]:
            cur_fish_position = candidate
    shark.eat(*cur_fish_position)


print(shark.time)
