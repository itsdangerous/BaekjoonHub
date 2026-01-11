N = int(input())
arr = list(map(int, input().split()))
B, C = map(int, input().split())

result = 0
for i in range(N):
    result += 1
    arr[i] = arr[i] - B
    if arr[i] > 0:
        result += arr[i] // C
        arr[i] = arr[i] % C
    if arr[i] > 0:
        result += 1

print(result)