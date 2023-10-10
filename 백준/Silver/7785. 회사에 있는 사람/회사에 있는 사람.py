N = int(input())
map = {}
cnt = 0
for i in range(N):
    name, cmd = input().split()
    if cmd == "enter":
        map[name] = 1
    elif cmd == "leave":
        if map.get(name) != None:
            map[name] = 0
            continue
        else:
            print("오류!! 들어오지 않았는데 나감")
            continue

reversed_map = {k: v for k, v in reversed(map.items())}

for key, value in sorted(reversed_map.items(), reverse=True):
    if value != 0:
        print(key)