from itertools import combinations_with_replacement

def solution(n, info):
    ry_scores = []
    
    for com in combinations_with_replacement(range(11),n):
        peach_score = 0
        r_score = 0
        lionList = [0]*11
        
        for idx in com:
            lionList[10-idx] += 1
        
        for i in range(11):
            if info[i] == lionList[i] == 0:
                continue
            if info[i] < lionList[i]:
                r_score += (10-i)
            else:
                peach_score += (10-i)
        
        diff = r_score - peach_score
        if diff > 0:
            ry_scores.append((diff,lionList[::-1]))
            
    ry_scores.sort(key = lambda x : (x[0],x[1]), reverse=True )
    
    if len(ry_scores) == 0:
        return [-1]
    else:
        return ry_scores[0][-1][::-1] 
        
    

"""
def solution(n, info):
    global answer, max_score
    # 1. 더 많은 k점을 맞춘 사람이 k점수를 가져간다.
    # 2. 단 같을 경우 어피치가 k점을 가져간다. (이전 대회 우승자가 양보)
    # 3. 만약 k점을 두 사람 모두 맞추지 못한 경우 아무도 k점을 가져갈 수 없다.
    # 4. 최종 점수로 우승자를 정하되, 최종 점수가 같다면 어피치가 우승자가 된다.
    # 라이언이 가장 큰 점수 차로 이기기 위해 쏴야할 점수 출력
    # 라이언이 우승 할 수 없는 경우(비기거나, 지는 경우)에는 [-1] return 
    
    # 큰 점수차로 이기기 위한 방법
    # 1. 어피치 0 점인거에 배치 x -> 라이언도 0 점
    # 2. 어피치가 맞춘거에서 큰 순서대로 ->  
    
    # 점수 차 리턴 함수
    def score(ryan):
        s = 0
        for i in range(11):
            # 둘 다 점수를 얻지 못하는 경우
            if ryan[i] == info[i] == 0:
                continue
            if ryan[i] > info[i]:
                s += 10-i
            else:
                s -= 10-i
        return s
    
    def dfs(idx, left, ryan):
        global answer, max_score
        # 남은게 있는데 인덱스가 -1 이면 종료(점수 만들 수 없는 경우)
        if idx == -1 and left :
            return
        # 점수를 만들 수 있는 경우
        if left == 0:
            s = score(ryan)
            # 현재 점수가 더 크면 정답 업데이트
            if max_score < s:
                answer = ryan[:] # 깊은 복사
                max_score = s
            return
        for i in range(left, -1, -1):
            ryan[idx] = i #10점 n개 쐈을때, 10점 n-1개 쐇을때 .. 로 분기
            dfs(idx-1,left-i,ryan) # 쏜 만큼 남은 화살에서 빼서 재귀
            ryan[idx] = 0
    
    answer = [0]*11
    max_score = 0
    ryan = [0]*11
    dfs(10,n,ryan)
    
    if max_score == 0:
        return [-1]
    else:
        return answer
"""
            
            