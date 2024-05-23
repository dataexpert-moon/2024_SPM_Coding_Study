def solution(picture, k):
    answer = []
    
    for pixel in picture:
        temp = ''
        for char in range(len(pixel)):
            temp += pixel[char] * k
        for _ in range(k):
            answer.append(temp)
        
    return answer