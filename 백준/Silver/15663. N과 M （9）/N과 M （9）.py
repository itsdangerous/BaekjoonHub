N, M = map(int, input().split())

arr = list(map(int, input().split()))

p = [-1] * M

dic = {}
visited = [False] * N
def solve(depth):
    if depth == M:
        nums_str = " ".join(map(str, p))
        dic[nums_str] = True
        return

    for i in range(N):
        if visited[i]: continue
        visited[i] = True
        p[depth] = arr[i]
        solve(depth+1)
        visited[i] = False

solve(0)

sorted_dic = sorted(dic.keys(), key=lambda x: tuple(map(int, x.split())))
print("\n".join(sorted_dic))
