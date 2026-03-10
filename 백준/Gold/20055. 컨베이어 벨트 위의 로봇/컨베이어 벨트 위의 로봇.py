
N, K = map(int, input().split())

arr = list(map(int, input().split()))

cnt = 0  # 내구도 0 칸
res = 0
robots = [False] * N

while cnt < K:
    res += 1
    # 한칸 회전
    # 1. 벨트 회전 - 벨트만 회전
    arr = [arr[-1]] + arr[:-1]
    # 2. 벨트 회전 - 로봇도 같이 회전
    robots = [False] + robots[:-1]
    robots[-1] = False

    # 3. 로봇 우측으로 1 움직임
    for i in range(N - 2, -1, -1):
        if robots[i]:  # 로봇이 있다면,
            if not robots[i + 1] and arr[i + 1] > 0:
                robots[i] = False
                robots[i + 1] = True
                arr[i+1] -= 1
                if arr[i+1] == 0:
                    cnt += 1

    # 마지막 떨궈주기
    robots[N - 1] = False

    # 4. 로봇 올리기
    if arr[0] > 0:
        robots[0] = True
        arr[0] -= 1
        if arr[0] == 0:
            cnt += 1

print(res)
