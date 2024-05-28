def solution(board, k):
    answer = 0
    
    row_len = len(board)
    col_len = len(board[0])
    
    for row_idx in range(row_len):
        for col_idx in range(col_len):
            if row_idx + col_idx <= k:
                answer += board[row_idx][col_idx]

    return answer