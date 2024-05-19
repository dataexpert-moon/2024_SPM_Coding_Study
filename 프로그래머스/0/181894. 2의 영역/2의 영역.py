def solution(arr):
    two_idx = []
    
    for idx in range(len(arr)):
        if(arr[idx] == 2):
            two_idx.append(idx)
    
    if not two_idx:
        return [-1]
    else:
        start = two_idx[0]
        end = two_idx[-1]
        return arr[start: end+1]
