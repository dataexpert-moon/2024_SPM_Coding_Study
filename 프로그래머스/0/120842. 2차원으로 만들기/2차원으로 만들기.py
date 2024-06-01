def solution(num_list, n):
    answer = []
    
    start = 0
    
    for _ in range(len(num_list) // n):
        answer.append(num_list[start:start+n])
        start += n
    
    if start != len(num_list):
        answer.append(num_list[start:])
    
    return answer