N, M = map(int, input().split())

arr = [i for i in range(1, N+1)]

for i in range(M) :
    a, b = map(int, input().split())
    a -=1
    b -=1
    arr[a], arr[b] = arr[b], arr[a]

for i in arr :
    print(i, end=' ')