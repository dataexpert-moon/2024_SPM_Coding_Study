def solution(str_list):
    for idx in range(len(str_list)):
        if str_list[idx] == 'l':
            if not str_list[:idx]:
                return list()
            else:
                return str_list[:idx]
        elif str_list[idx] == 'r':
            if not str_list[idx + 1:]:
                return list()
            else:
                return str_list[idx + 1:]
            
    return list()
                
        
    
    