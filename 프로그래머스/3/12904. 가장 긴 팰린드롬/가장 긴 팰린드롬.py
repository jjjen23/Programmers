def solution(s):
    answer = 0
    
    # 투 포인터로 해볼게
    # 인덱스를 조정하면서 대칭이면 최대 숫자 갱신
    # 해당 인덱스 기준 대칭일때까지 right이동
    
    # 실패한 이유1 : left를 땡겨서 조정해봐야함 그니까 처음부터 대칭이 아닐수도잇단소리임
    # 실패한 이유2 : 대칭이 전부 홀수일것이라고 가정한 나."abba"처럼 짝수일 수 있다. , 원소가 하나인 경우에 대해 고려안함.
    
    maxLen = 1 # 최소 한 글자는 항상 팰린드롬임!!
    
    # 해설참고
    # 하나의 중심에서 확장 -> 팰린드롬 길이 홀수
    # 두개의 중심에서 확장 -> 팰린드롬 길이 짝수
    
    def center(left,right):
        # 인덱스 범위 내이고, 오,왼이 같다면 1씩 늘려
        while left >=0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
    
    maxlen = 1 # 최소 팰린드롬의 길이는 1
    
    for i in range(len(s)):
        odd = center(i,i)
        even = center(i,i+1) 
        maxLen = max(maxLen, even, odd)
        
    answer = maxLen

    return answer



"""
 review: 하나의 인덱스를 중심으로 범위를 넓혀가는 접근 방식은 맞았다. 근데 짝수길이 팰린드롬 찾는법은 생각하지 못해서 답지를 참고
 
 방법1 : def solution(s):
    answer = 0
    
    # 투 포인터로 해볼게
    # 인덱스를 조정하면서 대칭이면 최대 숫자 갱신
    # 해당 인덱스 기준 대칭일때까지 right이동
    
    # 실패한 이유1 : left를 땡겨서 조정해봐야함 그니까 처음부터 대칭이 아닐수도잇단소리임
    # 실패한 이유2 : 대칭이 전부 홀수일것이라고 가정한 나."abba"처럼 짝수일 수 있다. , 원소가 하나인 경우에 대해 고려안함.
    
    maxLen = 1 # 최소 한 글자는 항상 팰린드롬임!!
    
    # 해설참고
    # 하나의 중심에서 확장 -> 팰린드롬 길이 홀수
    # 두개의 중심에서 확장 -> 팰린드롬 길이 짝수
    
    def center(left,right):
        # 인덱스 범위 내이고, 오,왼이 같다면 1씩 늘려
        while left >=0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
    
    maxlen = 1 # 최소 팰린드롬의 길이는 1
    
    for i in range(len(s)):
        odd = center(i,i)
        even = center(i,i+1) 
        maxLen = max(maxLen, even, odd)
        
    answer = maxLen

    return answer
    
    방법2(완전탐색) -> 효율성 시간초과:
    def solution(s):
        answer = 1 # 최소 한 글자는 항상 팰린드롬임!!

        for i in range(0,len(s)):
            for j in range(1, len(s)+1):
                if s[i:j] == s[i:j][::-1]:
                    answer = max(answer,len(s[i:j]))

    return answer
    

"""