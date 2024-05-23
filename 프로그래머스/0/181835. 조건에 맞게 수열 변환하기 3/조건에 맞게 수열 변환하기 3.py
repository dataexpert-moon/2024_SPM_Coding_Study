def solution(arr, k):
    
    if k % 2 == 1:
        for idx, num in enumerate(arr):
            arr[idx] = num * k
    else:
        for idx, num in enumerate(arr):
            arr[idx] = num + k
            
    return arr