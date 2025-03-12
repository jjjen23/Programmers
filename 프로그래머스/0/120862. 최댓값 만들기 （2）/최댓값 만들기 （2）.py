def solution(numbers):
    answer = 0
    numbers.sort()
    
    plusmax = numbers[-1] * numbers[-2]
    minusmax = numbers[0] * numbers[1]
    
    if plusmax > minusmax:
        answer = plusmax
    else:
        answer = minusmax
    
    return answer