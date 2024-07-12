def solution(nums):
    answer = 0
    nMari = len(nums) // 2
    nums = set(nums)
    
    if nMari > len(nums):
        answer = len(nums)
    else: answer = nMari
    return answer