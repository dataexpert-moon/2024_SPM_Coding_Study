def solution(num, k):
    num_list = list(map(int, str(num)))
    
    if num_list.count(k) != 0:
        return num_list.index(k) + 1
    else:
        return -1
        