def solution(arr, flag):
    answer = []
    
    for idx, value in enumerate(flag):
        if value:
            answer += [arr[idx]] * (arr[idx] * 2)
        else:
            for _ in range(arr[idx]):
                answer.pop()
                
    return answer