N, M, x, y, K = map(int, input().split())

arr = [[0]*M for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, input().split()))

commands = list(map(int, input().split()))
cube = [[0]*3 for _ in range(4)]


def rotate(d):
    global cube
    '''
     <원본>
     0 a 0
     b c d
     0 e 0
     0 f 0
     '''
    if d == 1:
        '''
        <동쪽> 
        0 a 0
        f b c
        0 e 0
        0 d 0'''
        t = cube[3][1]
        cube[3][1] = cube[1][2]
        cube[1][2] = cube[1][1]
        cube[1][1] = cube[1][0]
        cube[1][0] = t

    if d == 2:  # 서
        '''
        <서쪽>
        0 a 0
        c d f
        0 e 0
        0 b 0
        '''
        t = cube[3][1]
        cube[3][1] = cube[1][0]
        cube[1][0] = cube[1][1]
        cube[1][1] = cube[1][2]
        cube[1][2] = t

    if d == 3:  # 남
        '''
        <남쪽>
        0 f 0
        b a d
        0 c 0
        0 e 0
        '''
        t = cube[0][1]
        cube[0][1] = cube[3][1]
        cube[3][1] = cube[2][1]
        cube[2][1] = cube[1][1]
        cube[1][1] = t
    if d == 4:  # 북
        '''
        <북쪽>
        0 c 0
        b e d
        0 f 0
        0 a 0
        '''
        t = cube[0][1]
        cube[0][1] = cube[1][1]
        cube[1][1] = cube[2][1]
        cube[2][1] = cube[3][1]
        cube[3][1] = t

def update_val(r, c):
    # 주사위 바닥: [3, 1]
    if arr[r][c] == 0:
        # 주사위 바닥에 있는 값을 지도에 복사
        arr[r][c] = cube[3][1]
    else:
        cube[3][1] = arr[r][c]
        arr[r][c] = 0


def movable(r, c):
    return 0 <= r < N and 0 <= c < M


directions = [
    [0, 0],
    [0, 1],
    [0, -1],
    [-1, 0],
    [1, 0],
]
cur_pos = [x, y]
for cmd in commands:
    nr, nc = cur_pos[0] + directions[cmd][0], cur_pos[1] + directions[cmd][1]
    if not movable(nr, nc): continue
    cur_pos = [nr, nc]
    rotate(cmd)
    update_val(nr, nc)
    print(cube[1][1])