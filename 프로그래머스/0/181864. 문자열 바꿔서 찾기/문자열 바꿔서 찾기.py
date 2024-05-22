def solution(myString, pat):
    reverse_myString = ""
    for char in myString:
        if char == 'A':
            reverse_myString += 'B'
        else:
            reverse_myString += 'A'
    
    if pat in reverse_myString:
        return 1
    else:
        return 0
    