def solution(quiz):
    answer = []
    
    for question in quiz:
        cal = question.split("=")
        if eval(cal[0]) == eval(cal[1]):
            answer.append("O")
        else:
            answer.append("X")
    
    return answer