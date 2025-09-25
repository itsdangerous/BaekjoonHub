# import sys
# sys.stdin = open("input.txt", "r")

N = int(input())
P = int(input())

directions = [
    [-1, 0],
    [0, 1],
    [1, 0],
    [0,-1],
]

def print_arr(a):
    for i in range(N):
        for j in range(N):
            print(a[i][j], end=' ')
        print()
# 상우하좌 순으로 다음과 같이 증가함
'''
1, 1, 2, 2, 3, 3, 4, 4, ....
'''

# 제일먼저 중앙에서 시작해서, 방향별로 증가시킴

arr = [[-1] * N for _ in range(N)]
cnt = 0
d = 0
cur_r, cur_c = [N//2, N//2]
arr[cur_r][cur_c] = 1
v = 1
result_pos = [cur_r+1, cur_c+1]
while v < N*N:
    if d % 2 == 0: cnt += 1

    for _ in range(cnt):
        nr, nc = cur_r + directions[d][0], cur_c + directions[d][1]
        v = arr[cur_r][cur_c] + 1
        if v == P:
            result_pos = [nr+1, nc+1]

        if v > N*N:
            break
        arr[nr][nc] = v
        cur_r, cur_c = nr, nc
    d = (d + 1) % 4

print_arr(arr)
print(*result_pos)