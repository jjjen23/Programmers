import math 

def solution(array):
    answer = 0
    
    array.sort()
    idx = math.floor(len(array)//2)
    answer = array[idx]
    
    
    return answer