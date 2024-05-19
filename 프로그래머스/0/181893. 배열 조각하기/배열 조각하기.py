def solution(arr, query):
    
    for i, idx in enumerate(query):
        if i % 2 == 1: # 홀수일 때
            arr = arr[idx:]
        else: # 짝수일 때
            arr = arr[:idx+1]         
    
    return arr