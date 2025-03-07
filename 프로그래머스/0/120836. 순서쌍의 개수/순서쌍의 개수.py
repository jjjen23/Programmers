def solution(n):
    answer = 0
    tem = []
    
    # == 약수구하기 
    for i in range(1,int(n ** 0.5)+1):
        if n % i == 0:
            tem.append(i)
            if i < n//i:
                tem.append(n//i)
                
    
            
    answer = len(tem)
    
    return answer