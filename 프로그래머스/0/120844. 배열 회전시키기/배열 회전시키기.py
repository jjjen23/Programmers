def solution(numbers, direction):
    answer = []
    
    if direction == "left":
        for i in range(len(numbers)):
            idx = ((i+1) % len(numbers))
            answer.append(numbers[idx])
    else:
        for i in range(len(numbers)):
            idx = (i-1) % len(numbers)
            answer.append(numbers[idx])
        
    return answer