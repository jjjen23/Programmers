# 수리공 항승 # 실버3 # 그리디
# 가장 왼쪽에서 정수만큼 떨어진 거리>만< 물이 센다
# L의 길이를 가진 테이프를 이용해서 물을 막을 수 있는데 좌우 0.5만큼 간격을 줘야 물이 다시 안샘
# 항승이가 필요한 테이프의 최소 개수를 구하는 프로그램을 작성하라

n, l = map(int, input().split())
waterList = list(map(int,input().split()))

# 격차가 2이상 -> 2cm 테이프 필요
# 격차가 3이상 두 지점 -> 3cm 테이프 필요
# 그리디그리디..
# 한번 붙일때 x에 대해서 x-0.5 ~ x+0.5구간을 커버해야만 함
# l길이를 같이 적용한다고 치면 x-0.5 ~ x-0.5+l만큼 커버가 됨
# 끝 구간이 범위에 있는 요소만큼 퉁치고 범위 외에는 테이프 추가해주면 됨

waterList.sort()
answer = 0
end = 0

for w in waterList:
    if w + 0.5 <= end:
        continue
    answer += 1 # 테이프 추가
    end = w - 0.5 + l # 끝 갱신


print(answer)