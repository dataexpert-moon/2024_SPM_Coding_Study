from collections import deque


def is_valid(word, target):
    # 한 개의 알파벳만 다른지 체크
    diff_cnt = 0
    for i in range(len(target)):
        if word[i] != target[i]:
            diff_cnt += 1
        if diff_cnt > 1:
            return False
    return True


def solution(begin, target, words):
    q = deque()
    visited = {}

    for word in words:
        if is_valid(begin, word):
            q.append(word)
            visited[word] = 1

    while len(q) > 0:
        node = q.popleft()
        if node == target:
            return visited[node]
        for word in words:
            if word in visited or not is_valid(node, word):
                continue
            q.append(word)
            visited[word] = visited[node] + 1
    return 0


if __name__ == '__main__':
    begin = 'hit'
    target = 'cog'
    words = ["hot", "dot", "dog", "lot", "log", "cog"]
    sol = solution(begin, target, words)
    print(sol)