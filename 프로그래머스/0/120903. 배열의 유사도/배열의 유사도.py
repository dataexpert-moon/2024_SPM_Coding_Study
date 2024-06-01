def solution(s1, s2):
    answer = 0
    
    for char_s1 in s1:
        for char_s2 in s2:
            if char_s1 == char_s2:
                answer += 1

    return answer