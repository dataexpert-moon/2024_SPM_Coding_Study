def solution(my_string):
    answer = [0] * 52 
    
    for char in my_string: # ord는 문자열을 ASCII 코드로 변환 (A는 65, a는 97로 표현)
        if 'A' <= char <= 'Z':
            answer[ord(char) - ord('A')] += 1 
        elif 'a' <= char <= 'z':
             answer[ord(char) - ord('a') + 26] += 1 
    return answer