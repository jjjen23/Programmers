# 암기왕 실버 4
# 하루 동안 본 정수를 모두 수첩1에 적어놓았다.
# 수첩2에는 수첩1 중에 연종이 보았다고 주장한 수들을 적어놓았다.
# 수첩2에 적혀있는 순서대로, 각각의 수에 대하여 수첩 1에 있으면 1, 없으면 0을 출력
import sys
input = sys.stdin.readline

def binary_search(left,right,n_list,m):
    while left <= right:
        mid = (left + right) // 2
        if n_list[mid] == m:
            return 1
        else:
            if n_list[mid] < m:
                left = mid + 1
            else:
                right = mid - 1
    return 0


t = int(input())

for _ in range(t):
    n = int(input())
    n_list = list(map(int, input().split()))
    m = int(input())
    m_list = list(map(int, input().split()))

    # 시간 효율을 줄이기 위해 이분탐색으로 서치한다. -> 정렬 필수
    n_list.sort()
    # m_list.sort()

    for m in m_list:
        print(binary_search(0,n-1,n_list,m))


