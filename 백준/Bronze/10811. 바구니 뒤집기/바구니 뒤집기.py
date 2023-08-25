def reverse_arr(i: int, j: int, arr: list) -> None:
    index_left = i
    index_right = j
    while index_left <= (i + j) // 2:
        arr[index_left], arr[index_right] = arr[index_right], arr[index_left]
        index_left += 1
        index_right -= 1


N, M = map(int, input().split())

arr = [i for i in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    reverse_arr(a, b, arr)

for i in range(1, N + 1):
    print(arr[i], end=" ")