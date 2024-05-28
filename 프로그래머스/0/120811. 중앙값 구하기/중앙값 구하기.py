def solution(array):
    length = len(array)
    
    array.sort()
    
    return array[length // 2] 