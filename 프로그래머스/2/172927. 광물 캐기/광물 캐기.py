from collections import Counter

def solution(picks, minerals):
    answer = 0
    
    # 곡괭이 종류 당 5개 캐면 사용 x -> 사용시작 하면 무조권 5개
    # 광물을 전부 캐거나, 사용할 곡괭이가 없으면 종료
    # 광물은 주어진 순서로만
    
    if len(minerals) > 5*sum(picks):
        minerals = minerals[:5*sum(picks)]
        
    summary = []
    for i in range(0,len(minerals),5):
        cnt = Counter(minerals[i:i+5])
        summary.append((cnt['diamond'],cnt['iron'],cnt['stone']))
        
    # 다이아 -> 철 -> 돌 많은 순으로 정렬    
    summary.sort(reverse=True)
    
    answer = 0
    
    for nDia, nIron, nStone in summary:
        if picks[0] > 0:
            answer += nDia*1 + nIron*1 + nStone*1
            picks[0] -= 1
        elif picks[1] > 0:
            answer += nDia*5 + nIron*1 + nStone*1
            picks[1] -= 1
        elif picks[2] > 0:
            answer += nDia*25 + nIron*5 + nStone*1
            picks[2] -= 1
    
    return answer
    
