N, M = map(int, input().split())

arr = [0] * (N+1)

for i in range(M):
    a, b, c = map(int, input().split())
    for j in range(a, b+1):
        arr[j] = c
print(*arr[1:])