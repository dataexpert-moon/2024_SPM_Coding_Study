def solution(arr, queries):
    
    for row, col in queries:
        for idx in range(row, col + 1):
            arr[idx] += 1
    
    return arr
