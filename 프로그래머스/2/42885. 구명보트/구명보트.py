def solution(people, limit):
    people.sort()
    answer = 0
    
    # 투포인터 시작 - 끝 점
    start, end = 0, len(people) - 1
    # 동일할 때까지 시행
    while start <= end:
        # 2명 다 태울 수 있는 경우
        if people[start] + people[end] <= limit:
            start += 1
        end -= 1
        answer += 1
        
    return answer