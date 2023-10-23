def solution(s:str , skip:str, index:int):
    alpha_dict = [chr(i+97) for i in range(26) if chr(i+97) not in skip]
    answer = ""
    print(alpha_dict)
    for value in s :
        answer += cycle(skip, index, alpha_dict.index(value), alpha_dict)
    return answer

def cycle(skip:str, index:int, cur_index:int, alpha_dict:list) :

    len_alpha_dict = len(alpha_dict)
    result_index = cur_index + index
    if result_index > len_alpha_dict - 1 :
        result_index %= len_alpha_dict

    return alpha_dict[result_index]
            