def solution(n):
    answer = 0
    
    while n > 0:
        if n % 2 == 1: # 홀수
            answer += n
            n -= 2
        else:
            answer += n*n
            n -= 2
        
    return answer