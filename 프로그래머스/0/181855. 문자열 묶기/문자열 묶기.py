def solution(strArr):
    group = [0] * 31
    
    for str in strArr:
        group[len(str)] += 1
    
    return max(group)