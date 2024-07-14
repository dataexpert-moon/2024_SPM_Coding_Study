def solution(answers):
    answer = []
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    ac, bc, cc = 0, 0, 0
    
    for i in range(len(answers)):
        if answers[i] == a[i % len(a)]:
            ac += 1
        if answers[i] == b[i % len(b)]:
            bc += 1
        if answers[i] == c[i % len(c)]:
            cc += 1
            
    max_num = max(ac, bc, cc)
    
    if ac == max_num:
        answer.append(1)
    if bc == max_num:
        answer.append(2)
    if cc == max_num:
        answer.append(3)
        
    return answer