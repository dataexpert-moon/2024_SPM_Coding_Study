def solution(arr):
    power_of_2 = 1
    for _ in range(11):
        if power_of_2 >= len(arr):
            break
        else:
            power_of_2 *= 2
        
    return arr + [0] * (power_of_2 - len(arr))