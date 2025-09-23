from collections import deque  # 안 쓰면 제거해도 됨

N = int(input())

arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

nums = [i + 1 for i in range(N)]

group_1 = [-1] * (N//2)
group_1[0] = 1

group_2 = [-1] * (N//2)

min_v = -1
def calc_val(arr1: list):
    arr2 = []
    for i in nums:
        if i in arr1: continue
        arr2.append(i)

    sum_group_1 = 0
    sum_group_2 = 0
    for i in range(N//2):
        for j in range(N//2):
            sum_group_1 += arr[arr1[i]-1][arr1[j]-1]
            sum_group_2 += arr[arr2[i]-1][arr2[j]-1]

    return abs(sum_group_1 - sum_group_2)

def combination(start, depth):
    global min_v
    if depth == N // 2:
        v = calc_val(group_1)
        if min_v == -1:
            min_v = v
        else:
            min_v = min(min_v, v)
        return

    need = N//2 - depth
    for i in range(start, N - need + 1):
        group_1[depth] = nums[i]
        combination(i + 1, depth + 1)

combination(1, 1)
print(min_v)


