def solution(myString, pat):
    
    myString_lower = myString.lower()
    pat_lower = pat.lower()
    
    if len(myString_lower) < len(pat_lower):
        return 0
    
    if pat_lower in myString_lower:
        return 1
    
    return 0