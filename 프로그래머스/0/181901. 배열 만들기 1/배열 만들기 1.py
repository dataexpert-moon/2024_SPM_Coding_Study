def solution(n, k):
    answer = []
    
    for num in range(k, n+1, k):
        answer.append(num)
        
    return answer