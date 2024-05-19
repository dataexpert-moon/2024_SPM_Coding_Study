def solution(arr, queries):
    answer = []
    
    for row, col in queries:
        temp = arr[row]
        arr[row] = arr[col]
        arr[col] = temp
        

    return arr