def solution(arr, queries):
    
    for start, end, pivot in queries:
        for idx in range(start, end + 1):
            if idx % pivot == 0:
                arr[idx] += 1 
                
    return arr