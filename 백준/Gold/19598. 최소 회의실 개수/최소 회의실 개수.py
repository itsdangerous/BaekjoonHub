import heapq
import sys

N = int(sys.stdin.readline().rstrip())

arr = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
arr.sort(key=lambda x: x[0])

rooms = []
heapq.heappush(rooms, arr[0][1])

for i in range(1, N):
    if rooms[0] <= arr[i][0]:
        heapq.heappop(rooms)
    heapq.heappush(rooms, arr[i][1])

print(len(rooms))