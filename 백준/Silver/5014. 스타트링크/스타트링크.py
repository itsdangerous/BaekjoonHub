from collections import deque

full, start, dest, up, down = map(int, input().split())

# start -> dest로 가기 위해서 몇 버 버튼을 눌러야 하나?

visited = [False for _ in range(full + 1)]
time = -1
success = False
que = deque()
que.append(start)

while que and not success:
    # print(que)

    time += 1
    len_que = len(que)

    while len_que > 0:
        cur = que.popleft()
        visited[cur] = True
        if cur == dest:
            success = True
            break
        next_up = cur + up
        next_down = cur - down

        if (1 <= next_up <= full) and not visited[next_up]:
            visited[next_up] = True
            que.append(next_up)

        if (1 <= next_down <= full) and not visited[next_down]:
            visited[next_down] = True
            que.append(next_down)
        len_que -= 1

if success:
    print(time)
else:
    print("use the stairs")