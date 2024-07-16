"""
# 본래 답...
def solution(n):
    array = [True for i in range(n+1)]
    answer = 0

    for i in range(2, int(n**0.5) + 1):
        if array[i] == True:
            # i를 제외한 모든 배수 지우기(고로 j는 2부터 시작함)
            j = 2
            while i * j <= n:
                array[i*j] = False
                j += 1
    
    for i in range(2, n+1):
         if array[i] == True:
             answer += 1
    
    
    return answer
"""

# 간단하고 효율적인 버전
def solution(n):
    
    # 2부터 n까지의 집합 만들기
    array = set(range(2,n+1))
    
    # 이게 진짜 에라토스테네스의 체.. 아까 그건 범위만 줄인 것.
    # 에라토스테네스의 체 알고리즘은 범위 내에서 여러개의 소수를 구하는 문제(위 문제)에 적합
    for i in range(2, int(n**0.5) + 1):
        # 제거하지 않은 것 중 최소값
        if i in array:
            # 범위 내에서 i를 제외한 모든 i의 배수 제거
            array -= set(range(i*2, n+1, i))
    answer = len(array)
    
    return answer