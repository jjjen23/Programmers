# 링크드 리스트 : 딕셔녀리를 이용하여 열번호 : [prev열,next열]로 지정하면 된다. O(1) 
def solution(n, k, cmd):
    
    table = {i:[i-1,i+1] for i in range(n)}
    result = ['O']*n
    answer = ''
    delete_list = []
    pnt = k
    
    
    
    for command in cmd:
        command = command.split()
        
        if command[0] == 'D':
            for _ in range(int(command[1])):
                pnt = table[pnt][1]
        elif command[0] == 'U':
            for _ in range(int(command[1])):
                 pnt = table[pnt][0]
        
        # 삭제작업
        elif command[0] == 'C':
            prev, next = table[pnt]
            result[pnt] = 'X'
            delete_list.append((prev,pnt,next))
            
            # 현재가 마지막이라면 1칸 이전으로
            if next == n:
                pnt = table[pnt][0]
            else:
                pnt = table[pnt][1]
            
            # 삭제하려는값이 첫번째 요소일때
            if prev == -1:
                table[next][0] = prev
            # 삭제하려는 값이 마지막 요소일때
            elif next == n:
                table[prev][1] = next
            
            # 첫번째 ~ 마지막 사이 요소들
            else:
                table[prev][1] = next
                table[next][0] = prev
        # 복구작업
        else:
            prev,now,next = delete_list.pop()
            result[now] = 'O'
            
            if prev == -1:
                table[next][0] = now
            elif next == n:
                table[prev][1] = now
            # 마지막~끝 사이
            else:
                table[prev][1] = now
                table[next][0] = now
                
    # print(result)
    answer = ''.join(result)
    return answer


# 반쪽짜리 정답 -> 애초에 효율성도 실패이듯 -> 답지 -> 효율성 통과를 위해 링크드 리스트 쓰는 문제..
"""
 # 엄청난 난리의 흔적....
 def solution(n, k, cmd):
    
    def next_pnt(pnt,result,dist):
        now = 0
        while now != dist:
            pnt += 1
            if pnt == n:
                pnt = 0 # 오버플로우처리
                
            if result[pnt] == 'O':
                now += 1
        

        return pnt
    
    def next_pnt_minus(pnt,result,dist):
        now = 0
        while now != dist:
            pnt -= 1
            if pnt == -1:
                pnt = n-1 
                
            if result[pnt] == 'O':
                now += 1

        return pnt
    
    # 마지막 'O'인 인덱스를 찾는 함수
    def find_last(result):
        for i in range(n-1, -1, -1):
            if result[i] == 'O':
                return i
        return -1
    
    answer = ''
    delete_list = []
    pnt = k
    result = ['O']*n
    
    #변경할 점: pnt할때... n만큼 간다고 가정했을때, result[pnt] != 'X'인 기준으로 n만큼 간거임..!
    
    for command in cmd:
        
        if command[0] == 'C':
            result[pnt] = 'X'
            delete_list.append(pnt)
            
            # 마지막 행 삭제시 pnt는 바로 윗행으로
            if pnt == find_last(result):
                pnt = next_pnt_minus(pnt, result, 1)
            # 마지막 행 아니면 아래 행으로
            else:
                  pnt = next_pnt(pnt, result, 1)
            
        elif command[0] == 'Z':
            restored = delete_list.pop()
            result[restored] = 'O'
            
        elif command[0] == 'U':
            _, cnt = command.split(" ")
            pnt = next_pnt_minus(pnt,result,int(cnt)) 
            # pnt = (pnt-cnt) % n
            
        elif command[0] == 'D':
            _, cnt = command.split(" ")
            pnt = next_pnt(pnt,result,int(cnt)) 
            # pnt = (pnt+cnt) % n

    
    # print(result)
    answer = ''.join(result)
    return answer
"""