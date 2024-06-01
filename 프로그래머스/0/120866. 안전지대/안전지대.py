def solution(board):
 
    n = len(board)
    new_board = [row[:] for row in board]  # 깊은 복사
    
    bomb_directions = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    
    for x in range(n):
        for y in range(n):
            if board[x][y] == 1:
                for move_x, move_y in bomb_directions:
                    nx = x + move_x
                    ny = y + move_y
                    if 0 <= nx < n and 0 <= ny < n:
                        new_board[nx][ny] = 1
    
    count = 0
    
    for x in range(n):
        for y in range(n):
            if new_board[x][y] == 0:
                count += 1
    
    return count