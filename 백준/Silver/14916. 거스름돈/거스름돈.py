# 거스름돈 실버5 그리디
# 거스름돈이 n인 경우, 최소 동전의 개수가 몇 개인지 출력
# 2원 혹은 5원짜리로
# 일단 무조건 2또는 5로 나누어 떨어져야 함
# 5원을 max로 나눈다 -> 나머지가 2로 나누어지지 않으면 5몫을 하나씩 줄인다.
import sys
input = sys.stdin.readline

n = int(input())
answer = -1

# 5원을 최대한 많이쓰되, 2원으로 나누어떨어지면 정답
for i in range(n//5, -1, -1):
    remain = n - (5*i)
    if remain % 2 == 0:
        answer = i + (remain // 2)
        break

print(answer)




