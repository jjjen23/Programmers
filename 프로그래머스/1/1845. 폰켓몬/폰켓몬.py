def solution(nums):
    # 선택가능한 최대 종의 수가 답
    answer = 0
    nMari = len(nums) // 2
    nums = set(nums)
    
    # 집합을 이용해서 종의 수를 파악한다.
    
    # 만일 종의 수가 선택가능한 마리보다 작다면, 종의 수가 답(최대 종의 수니까.)
    if nMari > len(nums):
        answer = len(nums)
    else: answer = nMari
    return answer