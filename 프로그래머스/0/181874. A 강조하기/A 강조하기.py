def solution(myString):
    myString = list(myString)
    
    for idx, char in enumerate(myString):
        if char == 'a':
            myString[idx] = char.upper()
        elif char != 'A' and 'B' <= char <= 'Z':
             myString[idx] = char.lower()
    
    return ''.join(myString)