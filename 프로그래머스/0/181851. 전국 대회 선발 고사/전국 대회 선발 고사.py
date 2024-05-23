def solution(rank, attendance):
    
    exams = {}
    
    for idx, value in enumerate(attendance):
        if value:
            exams[idx] = rank[idx]
    
    exams_rank = dict(sorted(exams.items(), key=lambda x: x[1]))
    
    # 1,2,3등 뽑기
    first_student = list(exams_rank.keys())[0]
    second_student = list(exams_rank.keys())[1]
    third_student = list(exams_rank.keys())[2]

    # result 계산
    return 10000 * first_student + 100 * second_student + third_student


