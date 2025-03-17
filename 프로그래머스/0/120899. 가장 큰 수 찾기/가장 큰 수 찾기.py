def solution(array):
    max = 0
    idx = -1
    for i in range(len(array)):
        if array[i] > max:
            max = array[i]
            idx = i
    
    return [max,idx]