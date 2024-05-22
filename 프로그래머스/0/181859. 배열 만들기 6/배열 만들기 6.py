def solution(arr):
    stk = [] 
    idx = 0
    
    while (idx < len(arr)): 
        if not stk:
            stk.append(arr[idx])
        elif stk and stk[-1] == arr[idx]:
            stk.pop()
        elif stk and not stk[-1] == arr[idx]:
            stk.append(arr[idx])
            
        idx += 1
        
    if stk:
        return stk
    else:
        return [-1]
    
    
    
    
    
    
    
    
    
    
    
    
    
    return answer