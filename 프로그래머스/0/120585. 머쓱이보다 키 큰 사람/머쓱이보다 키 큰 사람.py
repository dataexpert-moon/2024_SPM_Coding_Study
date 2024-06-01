def solution(array, height):
    sorted_heights = sorted(array)
    count = 0
    
    for num in sorted_heights:
        if num <= height:
            count += 1
        else:
            break
        
    return len(array) - count