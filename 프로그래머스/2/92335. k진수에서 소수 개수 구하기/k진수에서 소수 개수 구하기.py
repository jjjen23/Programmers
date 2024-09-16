# 소수 판별 함수
def isPrime(n):
    for i in range(2,int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

remainList = ['0','1','2','3','4','5','6','7','8','9']

def solution(n, k):
    answer = 0
    chgnum = ''
    tem = []
    
    # 진법 변환하기
    while n != 0:
        tem.append(remainList[n % k])
        n //= k
        
    tem.reverse()   
    chgnum = ''.join(tem)
    # print(chgnum)
    
    # 변환한 진법에서 조건에 부합하는 소수 개수 찾기
    
    # 0기준으로 다 커트 해서 리스트에 쪼개서 저장 -> 1인건 드롭시킴 -> 소수인지 검사해서 소수일 시 +1 
    # 정규표현식? 사용하는게 편할까?  
    
    primeList = chgnum.split('0')
    
    realPrimeList = []
    for i in primeList:
        if i != '1' and i != '':
            realPrimeList.append(int(i))

        
    # print(realPrimeList)
    
    for n in realPrimeList:
        if isPrime(n):
            answer += 1
    
    return answer