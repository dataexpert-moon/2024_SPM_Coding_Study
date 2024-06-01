def solution(rsp):
    answer = ''
    win_conditions = {'2': '0', '5': '2', '0': '5'}
    
    for order in rsp:
        answer += win_conditions[order]

    return answer