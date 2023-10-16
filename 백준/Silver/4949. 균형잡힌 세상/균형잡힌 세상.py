from collections import deque

arr = []


def solve(s: str):
    result = "yes"
    que = deque()

    for i in s:
        # print(f"i = {i}")
        if i == "(":
            que.append(")")
        elif i == "[":
            que.append("]")
        elif i == ")":
            if que:
                if que.pop() != ")":
                    result = "no"
                    break
            else:
                result = "no"
                break
        elif i == "]":
            if que:
                if que.pop() != "]":
                    result = "no"
                    break
            else:
                result = "no"
                break
        elif i == ".":
            if que:
                result = "no"
                break
    arr.append(result)


while 1:
    s = input()
    if s == ".":
        break
    solve(s)

for i in arr:
    print(i)