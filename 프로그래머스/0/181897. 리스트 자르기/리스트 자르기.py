def solution(n, slicer, num_list):
    answer = []
     
    a = slicer[0] 
    b = slicer[1]
    c = slicer[2]
    
    if (n == 1):
        for num in range(0, b + 1):
            answer.append(num_list[num])
    elif (n == 2):
        for num in range(a, len(num_list)):
            answer.append(num_list[num])
    elif (n == 3):
        for num in range(a, b + 1):
            answer.append(num_list[num])
    elif (n == 4):
        for num in range(a, b + 1, c):
            answer.append(num_list[num])
    return answer