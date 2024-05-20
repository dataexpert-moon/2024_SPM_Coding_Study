def solution(strArr):
    for idx, str in enumerate(strArr):
        if idx % 2 == 1:
            strArr[idx] = strArr[idx].upper()
        else:
            strArr[idx] = strArr[idx].lower()
            
    return strArr