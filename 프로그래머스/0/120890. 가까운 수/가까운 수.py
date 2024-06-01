def solution(array, n):
    residual = abs(array[0] - n)
    answer = array[0]
    
    for num in array[1:]:
        temp = abs(num - n)
        if temp < residual:
            answer = num
            residual = temp
        
        elif temp == residual:
            answer = min(answer, num)
    
    return answer