def solution(myStr):
    answer = []
    
    for char in ['a', 'b', 'c']:
        myStr = myStr.replace(char, ' ')
    
    answer = myStr.split()
    
    if not answer:
        return ["EMPTY"]
    else:
        return answer
    
    
    