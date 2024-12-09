from collections import deque


def solution(n, k):
    dp = [1,1]
    answer = []
    for i in range(2,n+1):
        dp.append(dp[i-1]*i)
    # print(dp)
    
    deq = deque([i for i in range(1,n+1)])
    
    while n > 1:
        fac = dp[n-1]
        num = deq[(k-1)//fac]
        answer.append(num)
        deq.remove(num)
        n -= 1
        k %= fac
    
    answer.append(deq[-1])
    return answer