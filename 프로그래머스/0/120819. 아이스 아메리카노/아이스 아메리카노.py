def solution(money):
    answer = []
    coffee = 0
    
    while money >= 5500:
        coffee += 1
        money -= 5500
    
    answer.append(coffee)
    answer.append(money)
    
    return answer