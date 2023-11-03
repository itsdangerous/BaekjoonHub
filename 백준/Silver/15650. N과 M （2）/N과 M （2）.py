import sys

#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

N, M = map(int, input().split())

nums = [i + 1 for i in range(N)]

select_nums = [0 for _ in range(M)]

visited = [False for _ in range(N)]


def permutation(cnt: int, start: int):
    if cnt == M:
        print(*select_nums)
        return

    for i in range(start, N):
        if visited[i]:
            continue

        visited[i] = True
        select_nums[cnt] = nums[i]
        permutation(cnt + 1, i)
        select_nums[cnt] = 0
        visited[i] = False


permutation(0, 0)