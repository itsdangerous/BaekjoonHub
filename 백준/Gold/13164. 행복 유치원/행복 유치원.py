N, K = map(int, input().split())

arr = list(map(int, input().split()))

diff = sorted([arr[i] - arr[i - 1] for i in range(1, N)])

result = 0
for i in range(N - K):
    result += diff[i]
print(result)