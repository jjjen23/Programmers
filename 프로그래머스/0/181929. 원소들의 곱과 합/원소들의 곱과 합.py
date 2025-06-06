def solution(num_list):
    # 모든 원소 곱 < 모든 원소 합 제곱 -> 1 else -> 0
    mul , sumPower = 1, 0
    
    for i in num_list:
        mul *= i
        sumPower += i
    sumPower = sumPower ** 2
    
    if mul < sumPower :
        return 1

    return 0
