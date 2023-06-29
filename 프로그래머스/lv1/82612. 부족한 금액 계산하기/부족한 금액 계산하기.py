def solution(price, money, count):
    result = count/2*(1+count)*price - money
    return result if result > 0 else 0