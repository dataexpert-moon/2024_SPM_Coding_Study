def solution(n):    
    answer = 0
    
    for strnum in str(n):
        answer += int(strnum)
        
    return answer