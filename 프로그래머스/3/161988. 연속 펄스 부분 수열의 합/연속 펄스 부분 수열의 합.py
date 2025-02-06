def solution(sequence):
    answer = 0
    
    # 연속 펄스(-1 , 1 , -1 or 그 반대 부호) * 부분 수열의 합이 가장 큰 것을 출력하라.
    # 일단 넣어봐 숫자 그 다음에 뺐을때 더 크면 빼..  -> 투포인터 이용해보려고 했는데 잘 안됨 
    # 어떤 펄스든 결론적으로 두 펄스의 절대값은 동일함 -> 한 펄스만 구해서 양수화하면됨
    # 답지참고 -> dp활용
    # min(현재, 현재+)
    
    size = len(sequence)
    s1 = []
    s2 = []
    pulse = 1

    
    for i in range(size):
        s1.append(sequence[i] * pulse)
        s2.append(sequence[i] * (-pulse))
        
        pulse *= (-1)
    
    # print(s1)
    # print(s2)
    
    dp1, dp2 = [s1[0]], [s2[0]]
    
    
    # 현재랑, 이전 값+현재랑 더 큰것을 다음 dp에 갱신
    for i in range(1, size):
        dp1.append(max(s1[i], dp1[i-1]+s1[i]))
        dp2.append(max(s2[i], dp2[i-1]+s2[i]))
    
    # print(dp1)
    # print(dp2)
    
    answer = max(max(dp1),max(dp2))
    

    
    return answer