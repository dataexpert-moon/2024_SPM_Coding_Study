def solution(myString):
    answer = list()
    split_String = myString.split('x')
    
    for string in split_String:
        answer.append(len(string))
    return answer