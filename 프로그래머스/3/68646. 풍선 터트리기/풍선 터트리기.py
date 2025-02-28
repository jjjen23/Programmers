# 인전합 두 풍선 중 번호가 큰게 터짐(작은거 터지는 기회는 1번뿐)

def solution(a):
    if len(a) == 1:
        return 1
    
    answer = 2 # 양끝 값은 무조건 살아남을 수 있다.
    
    # 양끝에 위치한 풍선 -> 이전에 어떤 선택을 하던지, 최종선택에서 더 작은 풍선을 터트리는 기회가 한번 있으므로, 무조건 answer += 1 가능
    
    
    left_min = [a[0]] # 인덱스 위치별 왼쪽 최소값 배열
    right_min = [a[-1]] # 오른쪽 최솟값 배열
    
    
    # i위치까지의 오른쪽, 왼쪽에서 부터의 최소값을 저장해서 시간효율을 단축!!
    # dp방식으로 각자의 위치에서 최소값 확립해두기
    
    for i in range(1, len(a)):
        # 왼쪽 배열
        if a[i] < left_min[-1]:
            left_min.append(a[i])
        else:
            left_min.append(left_min[-1])
        # 오른쪽 배열
        if a[len(a)-1-i] < right_min[-1]:
            right_min.append(a[len(a)-1-i])
        else:
            right_min.append(right_min[-1])
    
    right_min.reverse()
    
    for i in range(1,len(a)-1):
        # 자신을 기준으로 양쪽 최솟값이 하나라도 자신보다 크면 끝까지 살아남을 수 있다. (원래는 양쪽 다 자신보다 커야 살아남을 수 있는데, 1번은 작은게 터질 수 있는 기회가 있기 때문에 괜찮다.
        # 큰거 나 큰거
        # 큰거 나 작은거
        # 작은거 나 큰거 
        # 이렇게 오면 안터진다 -> OR 조건 사용
        # = 양 쪽 최솟값이 둘 다. 자신보다 작다면 살아남을 수 없다.는 말과 동일하다.
        if left_min[i-1] > a[i] or right_min[i+1] > a[i]:
            answer += 1
    
    return answer

