def solution(num_str):
    answer = 0
    
    for idx in range(len(num_str)):
        answer += int(num_str[idx])
        
    return answer