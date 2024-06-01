def solution(s):
    answer = ''
    
    for str in s:
        if s.count(str) == 1:
            answer += str
    
    if not answer:
        return answer
    else:
        list_answer = sorted(list(answer))
        return ''.join(list_answer)
    