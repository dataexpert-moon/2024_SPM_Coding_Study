def solution(balls, share):
    def factorial(n):
        if n > 1:
            return n * factorial(n-1)
        else:
            return 1
    
    answer = factorial(balls) / (factorial(balls - share) * factorial(share))
    
    
    
    
    return answer