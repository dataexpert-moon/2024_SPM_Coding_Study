def solution(babbling):
    answer = 0
    pron = ["aya", "ye", "woo", "ma"]
    
    for i in babbling:
        result = 0
        for j in range(4): # 중복 불가
            if i.find(pron[j]) != -1:
                result += len(pron[j])
        if len(i) == result:
            answer += 1
        
    return answer