def solution(intStrs, k, s, l):
    answer = []
    
    for intStr in intStrs:
        conv_intStr = intStr[s:s+l]
        if (int(conv_intStr) > k):
            answer.append(int(conv_intStr))
        
    return answer