def solution(numbers):
    
    alpha_to_nums = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
                     'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    
    temp = ''
    answer = ''
    
    for num in numbers:
        temp += num
        if temp in alpha_to_nums.keys():
            answer += str(alpha_to_nums[temp])
            temp = ''
        
    return int(answer)