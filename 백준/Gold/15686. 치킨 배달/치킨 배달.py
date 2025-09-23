from itertools import combinations

n,m =map(int,input().split())

answer = 1e9

chicken, house = [],[]

for r in range(n):
    data = list(map(int,input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r,c))
        elif data[c] == 2:
            chicken.append((r,c))

# 모든 치킨 집 중 m개의 치킨집을 뽑는 조합
candid = list(combinations(chicken,m))

def get_sum(candid):
    res = 0
    for x1,y1 in house:
        tem = 1e9
        for x2,y2 in candid:
            tem = min(tem,abs(x1-x2)+abs(y1-y2))
        res += tem #각 집에서 가장 가까운 치킨집의 거리 더하기
    return res

for cand in candid:
    answer = min(answer,get_sum(cand))

print(answer)