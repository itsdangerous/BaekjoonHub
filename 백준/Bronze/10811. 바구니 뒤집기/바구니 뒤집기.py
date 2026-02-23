N, M = map(int, input().split())

arr = [i+1 for i in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    split_arrs = [arr[:a-1], arr[a-1:b], arr[b:]]
    split_arrs[1] = split_arrs[1][::-1]
    arr = split_arrs[0] + split_arrs[1] + split_arrs[2]
print(*arr)