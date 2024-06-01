def solution(spell, dic):
    answer = 2
    
    for word in dic:
        cnt = 0
        
        for alpha in spell:
            if alpha in word:
                cnt += 1
                
        if cnt == len(spell):
            answer = 1
            break
    
    return answer