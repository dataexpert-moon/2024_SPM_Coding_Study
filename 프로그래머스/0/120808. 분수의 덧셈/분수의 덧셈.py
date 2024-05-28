import math # 최대공약수를 구하기 위한 math 라이브러리

def solution(numer1, denom1, numer2, denom2):
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    gcd = math.gcd(numer,denom)
    
    return numer/gcd, denom/gcd