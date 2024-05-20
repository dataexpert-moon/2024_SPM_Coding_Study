def solution(arr):
    origin = arr
    cnt = 0
    
    while (True):
        new = list()
        for num in origin:
            if num >= 50 and num % 2 == 0:
                num /= 2
            elif num < 50 and num % 2 == 1:
                num = num * 2 + 1
            new.append(num)
                
        if new == origin:
            break
        else:
            cnt += 1
            origin = new
    
    return cnt