def solution(my_string):
    answer = ''
    
    for str in my_string:
        if str.isupper():
            answer += str.lower()
            continue
        answer += str
        
    return ''.join(sorted(answer))