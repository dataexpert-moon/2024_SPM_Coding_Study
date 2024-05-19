def solution(num_list):
    num_mul = 1 # 모든 원소들의 곱을 저장하는 변수
    num_sum = 0 # 모든 원소들의 합의 제곱을 저장하는 변수
    
    for num in num_list:
        num_mul *= num # 곱
        num_sum += num # 합
    
    num_sum_power = num_sum ** 2 # 제곱
    
    return 1 if num_mul < num_sum_power else 0