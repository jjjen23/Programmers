
def solution(n):
    answer = 0
    index = [1,2,4]
    tem = []
    while n != 0:
        n -= 1
        t = n % 3
        tem.append(str(index[t]))
        n //= 3
    tem.reverse()
    
    answer = ''.join(tem)
    
    return answer

