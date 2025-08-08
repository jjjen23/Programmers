# 용돈 관리
# M번만 인출가능
# 현우는 통장에서 K원을 인출 -> 하루를 보낼 수 있다면 그대로 사용,
# 모자라면 남은 금액은 통장에 집어넣고 다시 K원 인출

# 만일 남은 금액이 그날 사용할 금액보다 많더라도 남은 금액을 통장에
# 집어넣고 다시 K원 인출할 수 있다.
# 돈을 아끼기 위해 인출 금액 K를 최소화하기로 했다.
# 현우가 인출해야 할 최소 금액 K를 출력한다.

# 이진탐색

n, m = map(int,input().split())

withdraw = []
answer = 0

for _ in range(n):
    k = int(input())
    withdraw.append(k)

right = sum(withdraw)
left = max(withdraw)

while left <= right:
    cnt = 0
    total = 0
    mid = (left+right) // 2
    for i in withdraw:
        if total + i <= mid:
            total += i
        else:
            # 모자라면 다시 인출
            cnt += 1
            total = i #사용금액 재설정
    if total:
        cnt += 1



    # print(mid,cnt)

    if cnt <= m:
        right = mid-1
        answer = mid
    elif cnt > m:
        left = mid+1

print(answer)