def solution(num, total):
    
    avg = total // num
    start = avg - (num - 1) // 2
    
    answer = [start + i for i in range(num)]
    
    return answer