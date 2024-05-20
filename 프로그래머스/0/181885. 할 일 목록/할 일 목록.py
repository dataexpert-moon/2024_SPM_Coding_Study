def solution(todo_list, finished):
    answer = []
    
    for idx, value in enumerate(finished):
        if (not value):
            answer.append(todo_list[idx])
            
    return answer