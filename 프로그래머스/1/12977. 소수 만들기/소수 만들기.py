from itertools import combinations
# 소수란 1과 자기자신을 제외한 자연수로는 나누어 떨어지지 않는 자연수
def solution(nums):
    answer = 0
    
    # 3개 원소로 구성된 조합 생성
    combs = combinations(nums,3)
    
    for comb in combs:
        combSum = sum(comb)
        tem = 0
        for i in range(2, int(combSum**0.5)+1):
            if combSum % i == 0:
                tem = -1
        if tem == 0 :
            answer += 1

    return answer