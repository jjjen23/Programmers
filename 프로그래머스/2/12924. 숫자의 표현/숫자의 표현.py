def solution(n):
    answer = 0
    numlist = list(range(1,n+1))

    
    for i in range(len(numlist)):
        target = 0
        for j in range(i,len(numlist)):
            target += numlist[j]
            if target == n:
                answer += 1
                break
            elif target > n:
                break
                
    return answer