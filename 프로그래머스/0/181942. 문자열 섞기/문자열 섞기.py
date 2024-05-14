def solution(str1, str2):
    answer = ''
    for char in range(len(str1)):
        answer += str1[char]
        answer += str2[char]
    
    return answer