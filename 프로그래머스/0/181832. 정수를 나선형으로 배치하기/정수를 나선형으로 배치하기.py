def solution(n):
    answer = [[0] * n for _ in range(n)]
    
    # 시계방향 나선형 좌표 구성: 우, 하, 좌, 상
    dx = [0, 1, 0, -1] 
    dy = [1, 0, -1, 0]
    
    x, y = 0, 0
    
    # 초기값
    answer[x][y] = 1
    k = 2 # 값을 채울 변수
    
    # n*n까지 반복
    while k <= n * n:
        # 순차적으로 상하좌우 총 4번을 모두 살핀다
        for i in range(4):
            while True:
                nx = x + dx[i]
                ny = y + dy[i]
                
                # 주어진 범위를 벗어난다면 break
                if nx >= n or ny >= n or nx < 0 or ny < 0 or answer[nx][ny] != 0:
                    break
                else:
                    # 배열에 값을 채우고 x, y 좌표 위치 조정
                    answer[nx][ny] = k
                    x = nx
                    y = ny
                    k += 1
    
    return answer