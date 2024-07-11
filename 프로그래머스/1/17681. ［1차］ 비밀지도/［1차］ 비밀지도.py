# 벽:1 공백:0 -> 암호화에 쓰인 이진 연산법 : OR 연산법

def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        #5개로 길이 맞춰서 2진수로 채우기
        arr1[i] = bin(arr1[i])[2:].zfill(n)
        arr2[i] = bin(arr2[i])[2:].zfill(n)
        
        tem_ans = ''
        
        # OR연산
        for j in range(n):
            if arr1[i][j] == '1' or arr2[i][j] =='1':
                tem_ans += '#'
            else:
                tem_ans += ' '
        answer.append(tem_ans)
    
    return answer