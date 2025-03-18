def solution(n, cores):
    answer = 0
    
    
    if n <= len(cores):
        return n # 코어 번호 출력
    else:
        n -= len(cores)
        left = 1
        right = max(cores) * n # 작업 처리 최대시간
        
        # 이진탐색으로 작업에 필요한 최소 시간 찾기
        while left < right:
            mid = (left + right) // 2
            throughput = 0
            
            for core in cores:
                # mid초 까지 끝난 작업 개수
                throughput += mid // core
            
            # 처리 시간이 n보다 크거나 같은 값을 찾는다.
            if throughput >= n:
                right = mid
            else:
                left = mid+1
        
        print(right)

        # 찾은 최소시간 -1 까지 남은 작업 개수를 구한다.
        for core in cores:
            n -= (right - 1) // core
        
        
        # 마지막 작업 처리 코어 찾기
        for i in range(len(cores)):
            if right % cores[i] == 0:
                n -= 1
                if n == 0:
                    answer = i+1
                    break
                    
    return answer