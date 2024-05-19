def solution(arr, queries):
    # 1. 3차월 배열 구분
    # 2. 답이 존재하지 않으면 -1 저장
    
    answer = []
    
    for start, end, pivot in queries:
        temp = float('inf') # 매우 큰 수 초기화
        
        for idx in range(start, end + 1): 
            if (arr[idx] > pivot and arr[idx] < temp): # 조건에 맞는 답 추출
                temp = arr[idx]
        
        if (temp == float('inf')):
            answer.append(-1)
        else:
            answer.append(temp)

    return answer