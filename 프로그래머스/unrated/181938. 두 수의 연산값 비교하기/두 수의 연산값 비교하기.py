def solution(a, b):
    c, d = str(a), str(b)
    return max(int(c+d), 2*a*b)