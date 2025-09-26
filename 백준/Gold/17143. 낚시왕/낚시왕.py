import sys, copy
# sys.stdin = open("input.txt", "r")
R, C, M = map(int, input().split())

directions = [
    [-1, 0], # 상
    [0, 1], # 우
    [1, 0], # 하
    [0, -1], # 좌
]


def inline(r1, c1):
    global R, C
    return 0 <= r1 < R-1 and 0 <= c1 < C-1

def get_next_loc(i, j, speed, dir):

    if dir == 0 or dir == 2:  # i
        cycle = R * 2 - 2
        if dir == 0:
            speed += 2 * (R - 1) - i
        else:
            speed += i

        speed %= cycle
        if speed >= R:
            return (2 * R - 2 - speed, j, 0)
        return (speed, j, 2)

    else:  # j
        cycle = C * 2 - 2
        if dir == 3:
            speed += 2 * (C - 1) - j
        else:
            speed += j

        speed %= cycle
        if speed >= C:
            return (i, 2 * C - 2 - speed, 3)
        return (i, speed, 1)

class Shark:
    global arr

    def __init__(self, id, pos_r, pos_c, speed, direction, size):
        self.id = id
        self.r = pos_r
        self.c = pos_c
        self.speed = speed
        self.direction = direction
        self.size = size
        self.is_alive = True

    def move(self):
        if not self.is_alive: return
        time = self.speed
        origin_r, origin_c = self.r, self.c
        # while time > 0:
        #     time -= 1
        #     nr, nc = self.r + directions[self.direction][0], self.c + directions[self.direction][1]
        #     if not inline(nr, nc):
        #         self.direction = (self.direction + 2) %  4
        #         nr, nc = self.r + directions[self.direction][0], self.c + directions[self.direction][1]
        nr, nc, nd = get_next_loc(origin_r, origin_c, self.speed, self.direction)
        self.r, self.c, self.direction = nr, nc, nd
        # 원래 있던 자리 -1로
        arr[origin_r][origin_c] = -1

        # 이동한 shark의 위치는, 모든 shark가 이동한 후 한번에 arr에 찍어준다.

def print_list(l: list):
    for a in range(len(l)):
        for b in range(len(l[a])):
            print(l[a][b], end=' ')
        print()

arr = [[-1] * C for _ in range(R)]  # 가장 큰 물고기의 id가 존재하는 바다 배열

# sharks = []
sharks = {}
for case in range(M):
    # arr.append(list(map(int, input().split())))
    r, c, s, d, z = map(int, input().split())

    if d == 1:
        d = 0
    elif d == 2:
        d = 2
    elif d == 3:
        d = 1
    elif d == 4:
        d = 3
    shark = Shark(case, r-1, c-1, s, d, z)
    # sharks.append(shark)
    sharks[case] = shark
    arr[r-1][c-1] = shark.id
    # r,c : 좌표
    # s: 속력
    # d: 이동 방향
    # z: 사이즈

def delete_shark(shark_id):
    global arr, sharks
    sk = sharks[shark_id]
    sk.is_alive = False
    arr[sk.r][sk.c] = -1
    del sharks[shark_id]

result = 0
def simulation():
    global arr, result, sharks
    # 1. person move
        # 2. catch (collect sharks)
    for man_c in range(C):
        found_shark_id = None
        for r in range(R):
            if arr[r][man_c] != -1:
                found_shark_id = arr[r][man_c]
                break
        if found_shark_id is not None:
            found_shark = sharks[found_shark_id]
            if found_shark.is_alive:
                result += found_shark.size
                found_shark.is_alive = False
                delete_shark(found_shark_id)
                arr[found_shark.r][found_shark.c] = -1

        for k, v in sharks.items():
            v.move()

        # 4. 모든 샤크는 이동했으며, 같은 위치에 있는 경우 잡아먹는다.
        for k, sk in list(sharks.items()):
            if not sk.is_alive: continue
            prev_shark_id = arr[sk.r][sk.c]
            if prev_shark_id != -1: # 이미 해당 포지션에 shark id가 존재한다면,
                prev_shark = sharks[prev_shark_id]
                # 큰놈이 작은놈 잡아먹음
                # 크기가 같은 경우는 없음
                if sk.size > prev_shark.size:
                    prev_shark.is_alive = False
                    del sharks[prev_shark_id]
                    arr[sk.r][sk.c] = sk.id
                else:
                    sk.is_alive = False
                    del sharks[sk.id]
                    arr[prev_shark.r][prev_shark.c] = prev_shark.id
            else: arr[sk.r][sk.c] = sk.id
        sharks = sharks
        # print_list(arr)
        # print()

simulation()
print(result)