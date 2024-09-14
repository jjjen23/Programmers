
def solution(n, t, m, p):
    answer = ''
    
    # 가능한 나머지 리스트를 인덱스번호와 매칭해서 리스트 짬
    remainList = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    
    # 0은 모든 진법에서 0이므로 추가해주고 시작
    numbers = '0'
    
    # 최대 범위까지(t*m)전부 진법변환해서 구해두고, 내 차례만큼 정답에 추가하기 
    for i in range(1, t*m):
        
        tem = []
        # 진법 변환(몫이 0이 될때까지의 나머지값들 반대순서)
        while i > 0:
            tem.append(remainList[i%n])
            i //= n
        numbers += "".join(reversed(tem))
    
    #answer = numbers[p-1:t*m:m] #리스트 슬라이싱 이용가능
    for i in range(p-1, m*t, m):
        answer += numbers[i]
        
    return answer
