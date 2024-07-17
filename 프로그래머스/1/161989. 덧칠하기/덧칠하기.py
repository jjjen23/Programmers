def solution(n, m, section):
    answer = 0
    nList = [True for i in range(n)]
    
    for i in section:
        nList[i-1] = False
    
    for i in range(len(nList)):
        if nList[i] == False:
            answer += 1
            for j in range(m):
                if i+j < len(nList):
                    nList[i+j] = True
    
    return answer