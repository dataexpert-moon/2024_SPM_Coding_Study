def solution(array):
    answer = 0
    max_count = 0
    
    set_array = set(array)
    
    for value in set_array:
        count = array.count(value)
        if max_count < count:
            max_count = count
            answer = value
        elif max_count == count:
            answer = -1
    
    return answer