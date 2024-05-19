def solution(num_list):
    
    length = len(num_list)
    
    num_last_first = num_list[length - 1] # 마지막 원소
    num_last_second = num_list[length - 2] # 마지막에서 두 번째 원소
    
    
    if (num_last_first > num_last_second): # 마지막 원소 > 그전 원소
        num_list.append(num_last_first - num_last_second)
    else: # 마지막 원소 < 그전 원소
        num_list.append(num_last_first * 2) 
    
    return num_list