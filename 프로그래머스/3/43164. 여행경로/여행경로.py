def solution(tickets):
    graph = make_graph(tickets)
    
    stack = ["ICN"]  # ICN으로 시작
    answer = []
    
    while stack:
        top = stack[-1]
        
        if not graph[top]:  # 더 이상 이동할 공항이 없다면
            answer.append(stack.pop())  # 현재 공항 정보(= pop())를 answer에 저장
        else:
            stack.append(graph[top].pop())
            # top 공항과 연결된 공항 중 알파벳 순으로 가장 앞선 것을 pop
            # 해당 공항으로 이동한다.
    
    return answer[::-1]


def make_graph(tickets):
    from collections import defaultdict
    
    graph = defaultdict(list)
    for a, b in tickets:
        graph[a].append(b)
    
    for a in graph:
        graph[a].sort(reverse = True)  # 알파벳 역순으로 정렬
        
    return graph
