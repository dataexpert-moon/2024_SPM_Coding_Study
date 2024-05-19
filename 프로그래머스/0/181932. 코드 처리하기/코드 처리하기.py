def solution(code):
    mode = False
    ret = ''
    
    for idx, char in enumerate(code):
        if not mode:  # mode is 0
            if char != '1' and idx % 2 == 0:
                ret += char
            elif char == '1':
                mode = not mode
        else:  # mode is 1
            if char != '1' and idx % 2 == 1:
                ret += char
            elif char == '1':
                mode = not mode
    
    if ret == '':
        return 'EMPTY'
    return ret
