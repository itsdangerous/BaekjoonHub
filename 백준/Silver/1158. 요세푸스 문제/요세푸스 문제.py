from collections import deque

N, K = map(int, input().split())

que = deque([x + 1 for x in range(N)])
len_que = N
print("<", end="")
while len_que > 1:
    for i in range(K - 1):
        que.append(que.popleft())
    len_que -= 1
    print(que.popleft(), end=", ")
print(f"{que.popleft()}>")