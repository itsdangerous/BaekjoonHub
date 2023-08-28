N = int(input())

for i in range(N):
    arr = list(map(int, input().split()))
    arr.sort()
    print(arr[-3])