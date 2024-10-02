from collections import deque

def solution(prices):
    answer = []
    
    prices = deque(prices)
    
    while prices:
        tem = prices.popleft()
        cnt = 0
        for i in prices:
            if tem <= i:
                cnt += 1
            else:
                cnt+=1
                break
        answer.append(cnt)
        
    
    
    return answer

"""
def solution(prices):
    answer = []
    
    answer.append(0)
    # 거꾸로 가야할듯
    for i in range(len(prices)-2,-1,-1):
        temList = prices[i+1:]
        cnt = 0

        for j in temList:
            if prices[i]<=j:
                cnt+=1
            else:
                cnt+=1
                break
        answer.append(cnt)
        
    answer.reverse()
        
    
    
    return answer
"""