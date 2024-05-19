def solution(a, b, c, d):
    
    nums = {a, b, c, d} # 집합 생성
    
    if len(nums) == 4: # 조건1
        return min(nums)
    
    elif len(nums) == 1: # 조건2
        return nums.pop() * 1111
    
    # 주사위의 값이 몇번 나왔는지 (키, 값) 딕셔너리로 정리
    count = {}
    for num in (a, b, c, d):
        count[num] = count.get(num, 0) + 1 # num의 빈도를 세는 코드
    
    if len(nums) == 2: 
        if 3 in count.values(): # 조건3 
            p = [k for k, v in count.items() if v == 3][0] # count.items는 (키, 값)을 반환
            q = [k for k in nums if k != p][0] # 첫 번째 원소만 추출
            return (10 * p + q) ** 2
        else: # 조건4
            p, q = count.keys()
            return (p + q) * abs(p - q)
    else: # 조건5
        p = [k for k, v in count.items() if v == 2][0]
        q, r = [k for k in nums if k != p]
        return q * r
        
        
        
        
        
        
        
        
    