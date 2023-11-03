import sys
input = sys.stdin.readline

N, M = map(int, input().split())

nums = sorted(list(map(int, input().split())))

select_nums = [0 for _ in range(M)]

visited = [False for _ in range(N)]


def dfs(cnt: int):
    if cnt == M:
        print(*select_nums)
        return

    for i in range(N):
        if visited[i]:
            continue
        visited[i] = True
        select_nums[cnt] = nums[i]
        dfs(cnt + 1)
        select_nums[cnt] = 0
        visited[i] = False


dfs(0)