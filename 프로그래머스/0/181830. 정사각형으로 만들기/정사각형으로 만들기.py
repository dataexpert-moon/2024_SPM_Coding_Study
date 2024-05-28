def solution(arr):
    answer = [[]]
    
    row = len(arr)
    col = len(arr[0])
    
    if row == col:
        return arr
    elif row > col:
        for row_idx in range(row):
            for _ in range(row - col):
                arr[row_idx].append(0)
    else:
        for _ in range(col - row):
            arr.append([0] * col)
                
    return arr