def solution(sides):   
    cnt = 0

    # 나머지가 다른 두 변의 길이에 속할 때 
    cnt += sum(sides) - max(sides) - 1 
    
    # 나머지가 가장 긴 변의 길이일 때
    cnt += sum(sides) - max(sides)
    
    return cnt
