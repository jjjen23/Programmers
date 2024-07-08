def solution(n):
    list_3 = []
    answer = 0
    
    # 10진법 -> 3진법 변환
    # 나머지의 역순이 3진법으로 변환된 수
    while n > 0:
        list_3.append(n % 3)
        n = n // 3
    
    #리스트 인덱으를 이용한 계산을 위해 역순 배치
    list_3.reverse()
    
    # 3진법 -> 10진법 변환하기
    for i in range(len(list_3)):
        answer += (3 ** i) * list_3[i]       
    
    return answer