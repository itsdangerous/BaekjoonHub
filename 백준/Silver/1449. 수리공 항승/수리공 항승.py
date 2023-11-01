import sys

input = sys.stdin.readline

N, L = map(int, input().split())

arr = sorted(list(map(int, input().split())))

start_index = 0
cnt = 0
while start_index < N:
    if start_index == N - 1:
        cnt += 1
        break
    flag = False
    for end_index in range(start_index + 1, N):
        hap = arr[end_index] - arr[start_index] + 1
        if L == hap:
            cnt += 1
            start_index = end_index + 1
            break
        elif L < hap:
            cnt += 1
            start_index = end_index

            break
        if end_index == N - 1:
            cnt += 1
            flag = True
            break
    if flag:
        break

print(cnt)