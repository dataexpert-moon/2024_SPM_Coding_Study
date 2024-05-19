def solution(arr, intervals):
    answer = []
    
    for start, end in intervals:
        for idx in range(start, end + 1):
            answer.append(arr[idx])
            
    return answer