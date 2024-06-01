def solution(score):
    answer = []
    avg_score = []
    
    for i in score:
        avg_score.append(sum(i) / len(i))
    
    sort_avg_score = sorted(avg_score, reverse=True)
    
    for i in avg_score:
            answer.append(sort_avg_score.index(i) + 1)
        
    return answer