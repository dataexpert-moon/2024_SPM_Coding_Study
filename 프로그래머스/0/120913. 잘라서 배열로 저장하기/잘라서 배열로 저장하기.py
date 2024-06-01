def solution(my_str, n):
    answer = []
    start = 0
    
    for _ in range(len(my_str) // n):
        answer.append(my_str[start: start + n])
        start += n
    
    if start != len(my_str):
        answer.append(my_str[start:])
    
    return answer

