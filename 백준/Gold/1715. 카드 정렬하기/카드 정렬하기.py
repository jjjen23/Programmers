# A와 B를 묶으려면 A+B번의 비교 실행
import heapq

n = int(input())
cards = []

for i in range(n):
    tem = int(input())
    heapq.heappush(cards,tem)

# 최소 비교 횟수를 출력하라..
# 1. 일단 작은 수 부터 비교하는게 최소 아닐까
cards.sort()

answer = 0

while len(cards) > 1:

    oper1 = heapq.heappop(cards)
    oper2 = heapq.heappop(cards)
    answer += (oper1 + oper2)
    heapq.heappush(cards,oper1+oper2)
print(answer)