# 기둥은 바닥 위 OR 보의 한쪽 끝 부분 위에 있거나 OR 다른 기둥 위에 있어야 함
# 보는 한쪽 끝 부분이 기둥 위 OR 양쪽 끝 부분이 다른 보와 동시에 연결
# -> 규칙에 맞지 않으면 설치 x

# 기둥과 보 설치, 삭제 작업 순서대로 담긴 배열 -> 모든 명령어 수행 후 구조물 상태를 RETURN
# [x,y,a,b] 
# a :0은 기둥, 1은 보
# b :0은삭제, 1은 설치
# 좌표점 기준 보는 오른쪽 , 기둥은 위쪽 방향으로 설치 및 삭제


# 간과한 점 기둥과 보의 좌표가 같을 수 있다. 왜냐하면 보는 한쪽 끝 부분이 기둥 위에 오면 되니까...

# answer에 추가된거 기반으로 검증한다.
def is_valid(answer):
    for x,y,a in answer:
        if a == 0: #기둥
            # 조건: 바닥위, 보의 한쪽 끝 부분(오or왼), 다른 기둥 위
            if y == 0 or [x,y-1,0] in answer or [x-1,y,1] in answer or [x,y,1] in answer:
                continue
            return False
        else: #보
            
            #한쪽 끝 부분이 기둥 위 OR 양쪽 끝 부분이 다른 보와 동시에 연결
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x+1,y,1] in answer and [x-1,y,1] in answer):
                continue
            else:
                return False
    return True
            
def solution(n, build_frame):
    answer = []
    # x,y,a (좌표,기둥or보)
    # 정렬기준: 1.x좌표(y) 기준 오름차순, 2.y좌표(x) 기준 오름차순 3. a좌표 오름차순

    
    #풀때 x,y좌표 반대로 넣기
    for frame in build_frame:
        x,y,a,b = frame
        
        if b == 1: # 설치
            answer.append([x,y,a]) # 일단 추가하고 검증해
            if not is_valid(answer):
                # 유효하지 않으면(설치할 수 없다면) 제거
                answer.remove([x,y,a])
        else: #삭제
            answer.remove([x,y,a]) #일단 삭제해봐
            if not is_valid(answer):
                answer.append([x,y,a]) # 다시 추가해
            
    
    # 조건대로 정렬
    answer.sort(key=lambda x : (x[0],x[1],x[2]))
    
    return answer