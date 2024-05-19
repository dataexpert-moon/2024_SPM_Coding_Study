def solution(a, d, included):
    answer = 0
    ap = a
    
    for idx in range(len(included)):
        if included[idx]: # 
            answer += ap
        ap += d
            
    return answer