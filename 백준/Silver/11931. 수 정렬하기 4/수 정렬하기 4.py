import sys

input = sys.stdin.readline

#sys.stdin = open("input.txt", "r")

N = int(input())

arr = []
for i in range(N):
    arr.append(int(input()))

for i in sorted(arr, reverse=True):
    print(i)