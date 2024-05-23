def solution(n):
    answer = []
    
    for row in range(n):
        answer.append([])  
        for col in range(n):
            if row == col:
                answer[row].append(1)
            else:  
                answer[row].append(0)
    
    return answer