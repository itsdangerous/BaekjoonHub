from collections import deque


def print_arr_3(arr: list) -> None:
    print(f"time = {time} ----------------")

    for i in arr:
        for j in i:
            for k in j:
                print(k, end=" ")
            print()
        print()
    print(f"time = {time} ----------------")


def check_out_of_index(h: int, r: int, c: int) -> bool:
    return 0 <= h < H and 0 <= r < N and 0 <= c < M


direction = [[1, 0, 0], [-1, 0, 0], [0, -1, 0], [0, 0, 1], [0, 1, 0], [0, 0, -1]]
M, N, H = map(int, input().split())
visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]
not_success = 0
time = -1
que = deque()

arr = [[[int(x) for x in input().split()] for _ in range(N)] for _ in range(H)]

for h in range(H):
    for r in range(N):
        for c in range(M):
            if arr[h][r][c] == 1:
                que.append([h, r, c])
            if arr[h][r][c] == 0:
                not_success += 1
if not_success == 0:
    print(0)

else:
    while que:
        len_que = len(que)
        time += 1
        # print_arr_3(arr)

        while len_que > 0:
            pos = que.popleft()
            h, r, c = pos[0], pos[1], pos[2]
            visited[h][r][c] = True
            for dh, dr, dc in direction:
                # print(f"dh, dr, dc = {dh}, {dr}, {dc}")
                nh = h + dh
                nr = r + dr
                nc = c + dc
                # print(f"nh, nr, nc= {nh}, {nr}, {nc}")

                if not check_out_of_index(nh, nr, nc):
                    continue
                if visited[nh][nr][nc]:
                    continue
                if arr[nh][nr][nc] == -1:
                    visited[nh][nr][nc] = True
                    continue
                if arr[nh][nr][nc] == 1:
                    continue
                que.append([nh, nr, nc])
                visited[nh][nr][nc] = True
                arr[nh][nr][nc] = 1
                not_success -= 1
            len_que -= 1
    if not_success > 0:
        print(-1)
    else:
        print(time)