def solution(s):
    ctrlz = s.split()
    answer = int(ctrlz[0])
    temp = ctrlz[0]
    
    for x in ctrlz[1:]:
        if x == 'Z':
            answer -= int(temp)
        else:
            answer += int(x)
            temp = int(x)
    
    return answer