"""
# 에라토스테네스의 체 간단하고 간지버전...
def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)
"""

def solution(n):
    array = [True for i in range(n+1)]
    answer = 0
    # 이게 진짜 에라토스테네스의 체.. 아까 그건 복잡도만 줄인 것.
    # 에라토스테네스의 체 알고리즘은 여러개의 소수를 구하는 문제(위 문제)에 적합
    for i in range(2, int(n**0.5) + 1):
        if array[i] == True:
            # i를 제외한 모든 배수 지우기(고로 j는 2부터 시작함)
            j = 2
            while i * j <= n:
                array[i*j] = False
                j += 1
    
    # for i in range(2, n+1):
    #     if array[i] == True:
    #         answer += 1
    
    answer = array.count(True) - 2 #0,1 제외
    
    return answer