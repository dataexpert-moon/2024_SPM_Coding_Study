def solution(my_string, letter):
    answer = ''
    
    for char in my_string:
        if char == letter:
            continue
        answer += char
        
    return answer