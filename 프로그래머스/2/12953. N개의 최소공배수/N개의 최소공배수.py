def solution(arr):
    answer = 0
    
    while len(arr)  > 1:
        
        x_orign = arr.pop()
        y_orign = arr.pop()
        
        x, y = x_orign, y_orign
        
        while y:
            x, y = y, x % y
            
        arr.append((x_orign * y_orign) // x)
        
        
    answer = arr[0]    
    return answer