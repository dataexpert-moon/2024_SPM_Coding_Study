# 가로 * 세로 = 격자 합, 둘레의 합(가로*2 + 세로*2 - 겹치는부분 4) = 갈색 둘레

def solution(brown, red):
    for i in range(1, int(red**(1/2))+1):
        if red % i == 0:
            if 2*(i + red//i) == brown-4:
                return [red//i+2, i+2]