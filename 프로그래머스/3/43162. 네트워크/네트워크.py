def DFS(n, computers, com, visited):
    visited[com] = True  # 현재 컴퓨터를 방문 처리
    for connect in range(n):
        if connect != com and computers[com][connect] == 1:  # 현재 컴퓨터와 연결된 컴퓨터를 찾음
            if not visited[connect]:  # 아직 방문하지 않은 컴퓨터라면
                DFS(n, computers, connect, visited)  # DFS를 사용해 연결된 컴퓨터를 탐색

def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]  # 모든 컴퓨터를 방문하지 않은 상태로 초기화
    for com in range(n):  # 모든 컴퓨터를 확인
        if not visited[com]:  # 현재 컴퓨터가 방문되지 않았다면
            DFS(n, computers, com, visited)  # DFS를 사용해 연결된 모든 컴퓨터를 방문
            answer += 1  # 하나의 네트워크가 완성되었으므로 네트워크 수를 증가
    return answer
