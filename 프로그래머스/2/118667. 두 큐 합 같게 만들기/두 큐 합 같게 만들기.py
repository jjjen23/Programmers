from collections import deque

def solution(queue1, queue2):
    answer = 0
    # 두 개의 큐 합 // 2 -> 목표값 까지 최소 작업
    # FIFO
    # 목표 값보다 sum이 큰 큐에서 out -> sum 작은 큐에 집어넣기 : 작은큐 >=큰 큐 일때 까지 out -> in반복
    # 다시 작은 큐에서 같아질때 까지 out -> in 반복. 
    

    sumq1 = sum(queue1)
    sumq2 = sum(queue2)
    
    if (sumq1+sumq2) % 2 != 0:
        return -1
    
    target = (sumq1+sumq2) // 2
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    ans = 0
    # 두 큐가 완전 교환이 끝나서 기존 큐 두개의 값이 완전 히 뒤바뀐 상태가 되면 -1 
    max_moves = len(queue1) + len(queue2) +1
    
    while sumq1 != sumq2 and ans <= max_moves:
        if sumq1 > sumq2:
                tem = queue1.popleft()
                queue2.append(tem)
                sumq1 -= tem
                sumq2 += tem
        else:
                tem = queue2.popleft()
                queue1.append(tem)
                sumq2 -= tem
                sumq1 += tem
        ans += 1
        
    if sumq1 == sumq2 :
        answer = ans
    else:
        answer = -1
            
    return answer

print(solution([3,3,3,3], [3,3,21,3]))