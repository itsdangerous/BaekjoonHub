from collections import deque
N = int(input())
K = int(input())

arr = [[0]*N for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    arr[r-1][c-1] = 1

L = int(input())
que = deque()
for _ in range(L):
    x, c = input().split()
    que.appendleft((int(x), c))


# simulate
time = 0
head = [0, 0]
snake = deque()
snake.append(head)
directions = [
    [-1, 0],  # 상
    [0, 1],  # 우
    [1, 0],  # 하
    [0, -1]  # 좌
]
def check(r, c):
    return 0 <= r < N and 0 <= c < N

ahead = 1 # 우

tar_time, d = que.pop()
while True:
    time += 1
    nr, nc = head[0] + directions[ahead][0], head[1] + directions[ahead][1]
    if not check(nr, nc): break
    if arr[nr][nc] == 9:
        break
    if arr[nr][nc] == 1:
        # 사과 먹고 꼬리 그대로
        snake.append([nr, nc])
        arr[nr][nc] = 9
        head = [nr, nc]
    if arr[nr][nc] == 0:
        # 사과 먹고 꼬리 줄이기
        snake.append([nr, nc])
        arr[nr][nc] = 9
        head = [nr, nc]

        tail_r, tail_c = snake.popleft()
        arr[tail_r][tail_c] = 0

    if time == tar_time:
        if d == "D":
            ahead = (ahead + 1) % 4
        else:
            ahead = (ahead - 1) % 4

        if que:
            tar_time, d = que.pop()
print(time)