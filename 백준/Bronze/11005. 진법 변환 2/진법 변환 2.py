N, B = map(int, input().split())


def convert(a):
    if a >= 10:
        return chr(a + 55)
    return a


result = ""

while N >= B:
    result += str(convert(N % B))
    N = N // B

if N > 0:
    result += str(convert(N % B))
print(result[::-1])