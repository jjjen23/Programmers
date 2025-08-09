n = int(input())

arr = list(map(int,input().split()))
arr.sort()

cnt = 0

# 투포인터이용
for i in range(n):
    goal = arr[i]
    start = 0
    end = len(arr)-1

    while start < end:
        if arr[start] + arr[end] == goal:
            # 자기 자신을 합에 포함하면 안되니까 인덱스 체크
            if start == i:
                start += 1
            elif end == i:
                end -= 1
            # 자기 자신을 제외한 합일 때 cnt +1 하고 다음으로
            else:
                cnt += 1
                break
        # 이것을 위해 정렬 필수
        elif arr[start] + arr[end] > goal:
            end -= 1
        elif arr[start] + arr[end] < goal:
            start += 1

print(cnt)