from collections import deque
import sys

input = sys.stdin.readline
print = sys.stdout.write

stack = deque()
result = []


def stack_f(cmd: str):
    if cmd.split()[0] == "1":
        stack.append(cmd.split()[1])
    elif cmd.split()[0] == "2":
        if stack:
            result.append(stack.pop())
        else:
            result.append("-1")
    elif cmd.split()[0] == "3":
        result.append(str(len(stack)))
    elif cmd.split()[0] == "4":
        if stack:
            result.append("0")
        else:
            result.append("1")
    elif cmd.split()[0] == "5":
        if stack:
            result.append(stack[-1])
        else:
            result.append("-1")


N = int(input())

for i in range(N):
    stack_f(input())
for i in result:
    print(i + "\n")