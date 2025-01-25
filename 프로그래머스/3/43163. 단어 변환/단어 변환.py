from collections import deque

def solution(begin, target, words):
    
    if target not in words:
        return 0
    else:
        return bfs(begin, target, words)
        
def bfs(begin, target, words):
    queue = deque()
    queue.append([begin,0])

    while queue:
        now, step = queue.popleft()

        if now == target :
            return step

        for word in words:
            count = 0
            for i in range(len(word)):
                if now[i] != word[i]:
                    count +=1
            if count == 1:
                queue.append([word, step+1])
    return 0

