def convert(a):
    if "A" <= a <= "Z":
        return ord(a) - 55
    return int(a)


def solve():
    N, B = input().split()
    len_N = len(N)
    result = 0
    B = int(B)
    for index, value in enumerate(N):
        result += convert(value) * B ** (len_N - index - 1)

    return result


result = solve()
print(result)