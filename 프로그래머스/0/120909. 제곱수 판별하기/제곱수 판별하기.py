def solution(n):
    answer = 2
    
    square_idx = 1
    idx = 1
    
    while square_idx <= n:
        if square_idx == n:
            answer = 1
            break
        idx += 1
        square_idx = (idx * idx)
        
    return answer