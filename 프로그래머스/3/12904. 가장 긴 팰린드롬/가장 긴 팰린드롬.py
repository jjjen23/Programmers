def solution(s):
    answer = 0
    
    # 투 포인터로 해볼게
    # 인덱스를 조정하면서 대칭이면 최대 숫자 갱신
    # 해당 인덱스 기준 대칭일때까지 right이동
    
    # 실패한 이유1 : left를 땡겨서 조정해봐야함 그니까 처음부터 대칭이 아닐수도잇단소리임
    # 실패한 이유2 : 대칭이 전부 홀수일것이라고 가정한 나."abba"처럼 짝수일 수 있다. , 원소가 하나인 경우에 대해 고려안함.
    
    maxLen = 1 # 최소 한 글자는 항상 팰린드롬임!!
    
    # 하나의 중심에서 확장 -> 팰린드롬 길이 홀수
    # 두개의 중심에서 확장 -> 팰린드롬 길이 짝수
    
    def center(left,right):
        # 인덱스 범위 내이고, 오,왼이 같다면 1씩 늘려
        while left >=0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
    
    maxlen = 1 # 최소 팰린드롬의 길이는 1
    
    for i in range(0,len(s)):
        odd = center(i,i)
        even = center(i,i+1) 
        maxLen = max(maxLen, even, odd)
        
    answer = maxLen

    return answer



"""
def solution(s):
    answer = 0
    
    # 투 포인터로 해볼게
    # 인덱스를 조정하면서 대칭이면 최대 숫자 갱신
    # 해당 인덱스 기준 대칭일때까지 right이동
    
    # 실패한 이유1 : left를 땡겨서 조정해봐야함 그니까 처음부터 대칭이 아닐수도잇단소리임
    # 실패한 이유2 : 대칭이 전부 홀수일것이라고 가정한 나."abba"처럼 짝수일 수 있다. , 원소가 하나인 경우에 대해 고려안함.
    
    maxLen = 1 # 최소 한 글자는 항상 팰린드롬임!!
    s = list(s)
    
    for i in range(1,len(s)):
        tem = s[:i+1]
        tem = tem[::-1]
        # print(tem)
        j = i
        if tem == s[i:i+i+1]:
            # 갱신
            maxLen = max(maxLen, (i*2+1))
        else:
            # i가 1일때까지 i를 1씩 빼서 비교한다.
            while j > 1 :
                j -= 1
                tem = s[i-j:i+1]
                tem = tem[::-1]
                # print("tem",tem)
                # print("other",s[i:i+j+1])
                if tem == s[i:i+j+1]:
                    # 갱신
                    maxLen = max(maxLen, (j*2+1))
                    break
                
                
    answer = maxLen    
    

    return answer
"""