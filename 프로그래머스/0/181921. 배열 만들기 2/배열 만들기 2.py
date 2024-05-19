def solution(l, r):
    answer = []
    
    for num in range(l, r + 1): # l과 r 범위 설정
        is_valid = True # 0 또는 5가 아닌 경우의 개수
        str_num = str(num) # 문자로 변경
    
        for char in str_num: # 각 자리의 숫자 확인
            if (char != '0' and char != '5'): # 0과 5를 만족하지 않았다면
                is_valid = False
                break
        
        if is_valid: # 숫자가 0과 5로 이루어졌다면
            answer.append(num)
            
    if not answer: # 조건에 맞는 정수가 없다면
        answer.append(-1)
        
    return answer