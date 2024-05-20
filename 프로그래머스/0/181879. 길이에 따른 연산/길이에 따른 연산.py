def solution(num_list):
    answer = 0
    
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        return eval('*'.join([str(n) for n in num_list]))
