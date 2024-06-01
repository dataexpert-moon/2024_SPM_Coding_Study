def solution(keyinput, board):
    answer = [0, 0]
    # 위 아래 왼쪽 오른쪽
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    direction_keys = ["up", "down", "left", "right"]
    
    max_x = board[0] // 2
    max_y = board[1] // 2
    
    for key in keyinput:
        idx = direction_keys.index(key)
        nx = answer[0] + dx[idx]
        ny = answer[1] + dy[idx]
        if -max_x <= nx <= max_x and -max_y <= ny <= max_y:
            answer[0] = nx
            answer[1] = ny
            
    return answer