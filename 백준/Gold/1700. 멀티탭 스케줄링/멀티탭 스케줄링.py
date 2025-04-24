# 멀티탭 스케줄링 # 그리디 #골드1
# 플러그 빼는 횟수 최소화
# n은 멀티탭의 구멍 개수
from collections import deque

n, k = map(int, input().split())
toolList = list(map(int,input().split()))

toolList = deque(toolList)

# 1. 뒤에 현재 스택에 존재하는 요소가 있다면 걔말고 다른 애를 바꾼다.
# 2. 뒤에 현재 스택에 존재하는 요소가 모두 있다면 더 적게 카운트 된 애를 뺀다?
stack = []
answer = 0
while len(toolList) > 0:
    tem = toolList.popleft()

    # 스택에 존재할 떄
    if tem in stack:
        continue
    # 존재하지 않을 때
    else:
        # 스택에 여유가 있을때 -> 추가
        if len(stack) < n:
                stack.append(tem)
        # 스택에 여유가 없을때 -> 교체
        else:
            dict1 = {}
            for s in stack:
                if s in toolList:
                    dict1[s] = toolList.index(s) # 가장 빨리 다시 나올 위치 저장
                else:
                    dict1[s] = float('inf') #앞으로 안나오는 애들은 무한대값 설정
            # 가장 늦게 나올 친구를 빼는 전략(아예안나오거나 혹은 가장 늦게 나오거나)
            to_remove = max(dict1, key=dict1.get)
            stack.remove(to_remove)
            stack.append(tem) # 제거 후 추가
            answer += 1

print(answer)


