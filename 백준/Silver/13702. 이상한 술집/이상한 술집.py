# 이상한 술집
# 실버 2
# 막걸리를 N 주전자 주문하고, 본인 포함 친구들 K명에게 막걸리를 똑같은 양으로 나누어준다.
# 다른 주전자의 막걸리가 섞이는게 싫어서 주전자에 막걸리가 애매하게 남아있으면 걍 버리기로 한다. -> 나머지는 버리고 몫만
# K명에게 최대한 많은 양의 막걸리를 분배할 수 있는 용량을 출력하라

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nambee = []
for i in range(n):
    nambee.append(int(input()))

left = 1 # 초기값을 잘 잡자!!!!
right = max(nambee)
answer = 0

# 항상 이분탐색 종료 조건은 <=
while left <= right:
    mid = (left + right) // 2
    sum = 0

    for i in nambee:
        sum += i // mid

    # k명에게 똑같은 용량으로 나누어 줄 수 있다면~ 정답 갱신 후 용량 upup
    if sum >= k:
        answer = mid
        left = mid + 1

    else:
        right = mid - 1

print(answer)