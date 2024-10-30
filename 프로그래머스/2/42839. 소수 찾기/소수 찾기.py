from itertools import permutations

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    numset = set()
    for i in range(1,len(numbers)+1):
        for com in permutations(numbers,i):
            tem = ''.join(com)
            tem = int(tem)
            if tem != 0 and tem != 1:
                numset.add(tem)
    # print(numset)
    
    # 여러개의 소수판별 : 에레..스토스어쩌구의 체
    for num in numset:
        flag = True
        for j in range(2,int(num**0.5)+1):
            if num % j == 0:
                flag = False
                break
        if flag == True:
            answer += 1
                
    return answer
