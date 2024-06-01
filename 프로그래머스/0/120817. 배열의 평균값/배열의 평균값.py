def solution(numbers):
    len_numbers = len(numbers)
    sum = 0
    
    for num in numbers:
        sum += num
    
    return sum / len_numbers 