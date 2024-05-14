def solution(my_string, overwrite_string, s):
    answer = ''
    overwrite_length = len(overwrite_string)
    # divide and conquer
    # 1. 인덱스 앞
    for i in my_string[:s]:
        answer += i
    # 2. 인덱스부터 overwrite
    for j in overwrite_string:
        answer += j
    # 3. overwrite부터 끝까지
    for k in my_string[s+overwrite_length:]:
        answer += k
    return answer