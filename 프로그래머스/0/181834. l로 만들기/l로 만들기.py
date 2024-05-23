def solution(myString):
    answer = ''
    
    for lower in myString:
        if ord(lower) < ord('l'):
            answer += 'l'
        else:
            answer += lower
            
    return answer