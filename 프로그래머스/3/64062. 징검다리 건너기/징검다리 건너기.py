# 몇 명이 징검다리를 건널 수 있는지 출력
# stone은 밟을 때 마다 -1
# 모든 돌을 밟을 수 있다면 +1 칸씩
# 아니라면 가장 가까운 돌 뛰어넘기 (뛰는 길이는 k개 이하로 한정되어 있다.)
# 뛰어넘을 수 있는 돌이 k개 초과일때 종료, answer return

# 일단 함수 두개를 분리해서 만들자. 재귀적으로 호출해야 할 것 같음 -> 아 잘 안됨 짜증남!!!! 

            

# 이진탐색 활용 : 탐색범위 1 ~ 건널 수 있는 최대사람 수
def solution(stones, k):
    
    answer = 0
    
    Min = 1
    Max = max(stones)
    
    while Min <= Max:
        count = 0 # Mid를 최대사람 수로 가정했을 때 건널 뛰게 될 간격(0이하의 칸 수 측정) 
        Mid = (Min + Max) // 2
        
        for s in stones:
            if s - Mid <= 0:
                count += 1
            else:
                count = 0 # 0초과하는 돌은 거기서부터 다시 측정
                
            if count == k: #건너뛸 수 있는 최대
                answer = Mid
                break
        
        # 현재 인원수가 건너뛸수있는 최대 간격보다 k가 더 크다면 상향조정
        if count < k:
            Min = Mid + 1
        else:
            answer = Mid
            Max = Mid - 1
        
    
    return answer

"""
def solution(stones, k):
    
    answer = 0
    left = 1 #배열 원소들의 값은 1 이상이므로 1부터가 최소!
    right = max(stones)
    
    while left <= right:
        count = 0
        mid = (left+right) // 2
        
        #k는 한번에 건너 뛸 수 있는 칸 수!
        
        for s in stones:
            if s - mid <= 0:
                # 연속된 0 이하 카운트
                count+=1
            else:
                # 0 초과일땐 다시 0 부터 카운트
                count = 0
        
            if count == k:
                break
                
        # 인원수 크게 재조정
        if count < k :
            left = mid+1
            
        # 인원수 작게 재조정
        else:
            right = mid - 1
            answer = mid
        
    
    
    return answer
"""


"""
    내가 푼 방법1: # 일단 함수 두개를 분리해서 만들자. 재귀적으로 호출해야 할 것 같음 -> 아 잘 안됨 짜증남!!!! -> 효율성에서 떨어질 거 같음.. 이외는 생각 안나서 답지 보기로함
    
    def search(start, stones, answer,k):
    while True:
        for i in range(start,len(stones)):
            if stones[i] != 0:
                stones[i] -= 1
            else:
                # 어디까지 점프할지 헤아리는 함수
                new_start = jump(i, stones,k)

                if new_start is False:
                    return answer # 종료 조건만족, 반환
                else:
                    search(new_start, stones, answer,k)
                    # start = new_start
                    # break
        answer += 1
    

            
# 2. 어디까지 점프할지 헤아리는 함수
def jump(start, stones,k):
    j = 0
    while  start+j < len(stones) and stones[start+j] == 0:
        if j > k: 
            return False
        else:
            j += 1
        
    return start+j # k이하면 점프 할 위치 반환
            

def solution(stones, k):
    answer = 0
    
    answer = search(0, stones, answer, k)
    
    return answer
    
    답지 : 이진탐색을 활용했어야 함...이렇게 간편하다니. ㄱ-
    
"""