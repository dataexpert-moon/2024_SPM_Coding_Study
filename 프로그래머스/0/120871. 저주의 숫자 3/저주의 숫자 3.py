def solution(n):
    answer = 0
    ten_num = 0
    
    while ten_num < n:
        answer += 1
        
        while '3' in str(answer) or answer % 3 == 0:
             answer += 1
        
        ten_num += 1
        
    return answer
        

    