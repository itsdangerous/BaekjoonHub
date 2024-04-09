N = int(input())

str = input()

M = 1
for i in str:
    if i != "C":
        M += 1
print(N // M)
