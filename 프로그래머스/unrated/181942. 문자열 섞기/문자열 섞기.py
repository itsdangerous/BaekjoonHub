def solution(str1, str2):
    arr = [0]*len(str1)*2
    for i in range(0, len(arr), 2) :
        arr[i], arr[i+1] = str1[i//2], str2[(i+1)//2]
    
    return ''.join(arr)