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

def get_next_loc(r, c, speed, d):
    # 좌 우
    if d in (1, 3):
        cycle = 2 * C - 2
        if d == 1: # 우
            speed += c
        else: # 좌
            speed += 2*C-2 - c
        speed = speed % cycle
        if speed >= C:
            return r, 2*C-2-speed, 3
        return r, speed, 1

    # 상 하
    elif d in (0, 2):
        cycle = 2*R - 2
        if d == 2: # 하
            speed += r
        else:
            speed += 2*R-2 - r
        speed = speed % cycle
        if speed >= R:
            return 2*R-2-speed, c, 0
        return speed, c, 2

class Shark:
    global arr

    def __init__(self, id, pos_r, pos_c, speed, direction, size):
        self.id = id
        self.r = pos_r
        self.c = pos_c
        self.speed = speed
        self.direction = direction
        self.size = size

    def move(self):
        origin_r, origin_c = self.r, self.c

        nr, nc, nd = get_next_loc(origin_r, origin_c, self.speed, self.direction)
        self.r, self.c, self.direction = nr, nc, nd
        # 원래 있던 자리 -1로
        arr[origin_r][origin_c] = -1

        # 이동한 shark의 위치는, 모든 shark가 이동한 후 한번에 arr에 찍어준다.

arr = [[-1] * C for _ in range(R)]  # 가장 큰 물고기의 id가 존재하는 바다 배열

sharks = {}
for case in range(M):
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
    sharks[case] = shark
    arr[r-1][c-1] = shark.id

def delete_shark(shark_id):
    global arr, sharks
    sk = sharks[shark_id]
    arr[sk.r][sk.c] = -1
    del sharks[shark_id]

result = 0
def simulation():
    global arr, result, sharks
    # 1. person move
    for man_c in range(C):
        # 2. catch (collect sharks)
        found_shark_id = None
        for r in range(R):
            if arr[r][man_c] != -1:
                found_shark_id = arr[r][man_c]
                break
        if found_shark_id is not None:
            found_shark = sharks[found_shark_id]
            result += found_shark.size
            delete_shark(found_shark_id)
            arr[found_shark.r][found_shark.c] = -1

        for k, v in sharks.items():
            v.move()

        # 3. 모든 샤크는 이동했으며, 같은 위치에 있는 경우 잡아먹는다.
        for k, sk in list(sharks.items()):
            prev_shark_id = arr[sk.r][sk.c]
            if prev_shark_id != -1: # 이미 해당 포지션에 shark id가 존재한다면,
                prev_shark = sharks[prev_shark_id]
                # 큰놈이 작은놈 잡아먹음
                # 크기가 같은 경우는 없음
                if sk.size > prev_shark.size:
                    del sharks[prev_shark_id]
                    arr[sk.r][sk.c] = sk.id
                else:
                    del sharks[sk.id]
                    arr[prev_shark.r][prev_shark.c] = prev_shark.id
            else: arr[sk.r][sk.c] = sk.id
        sharks = sharks

simulation()
print(result)