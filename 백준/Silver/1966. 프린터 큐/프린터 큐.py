T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    l = list(map(int, input().split()))
    max_num = max(l)
    arr = []
    for i in range(N):
        arr.append([l[i], i])

    # M번째가 index가 몇번째에 꺼내지는지
    # 왼쪽부터 꺼내짐
    cnt = 0
    while arr:
        if arr[0][0] < max_num:
            tmp = arr[0]
            arr = arr[1:]
            arr.append(tmp)
            continue
        else:
            cnt += 1
            if arr[0][1] == M:
                break
            else:
                origin_index = arr[0][1]
                l[origin_index] = -1
                max_num = max(l)
                arr = arr[1:]
                continue

    print(cnt)