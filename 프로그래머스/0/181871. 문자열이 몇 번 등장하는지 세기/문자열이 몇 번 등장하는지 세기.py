def solution(myString, pat):
    cnt = 0
    len_pat = len(pat)
    
    for idx in range((len(myString) - len_pat) + 1):
        if myString[idx:idx+len_pat] == pat:
            cnt += 1
    
    return cnt