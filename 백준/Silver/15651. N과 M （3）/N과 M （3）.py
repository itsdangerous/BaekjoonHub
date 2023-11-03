from itertools import product

n, m = map(int, input().split())

arr = [i for i in range(1, n+1)]

result = product(arr, repeat=m)

for i in result :
    for j in i :
        print(j, end=' ')
    print()