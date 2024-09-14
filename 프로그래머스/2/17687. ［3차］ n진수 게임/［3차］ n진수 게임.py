def solution(n, t, m, p):
    answer = ''
    
    remainList = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    
    numbers = '0'

    for i in range(1, t*m):
        
        tem = []
        while i > 0:
            tem.append(remainList[i%n])
            i //= n
        numbers += "".join(reversed(tem))
    
    #answer = numbers[p-1:t*m:m] #리스트 슬라이싱 이용가능
    for i in range(p-1, m*t, m):
        answer += numbers[i]
        
    return answer
