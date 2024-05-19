def solution(arr, idx):
 
    for answer in range(idx, len(arr)):
        if arr[answer] == 1:
            return answer
        
    return -1