def solution(numbers):
    origin = [0,1,2,3,4,5,6,7,8,9]
    
    # numbers 배열에 있는건 제거하여 합 구하기
    for num in numbers:
        if num in origin:
            origin.remove(num)
                
    answer = sum(origin)
    
    return answer