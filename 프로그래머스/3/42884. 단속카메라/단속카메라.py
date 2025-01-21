def solution(routes):
    answer = 0
    
    # 진출 지점 기준
    camera = -30001
    
    routes.sort(key=lambda x : x[1])
    
    for route in routes:
        # 카메라가 진입 지점보다 작은지 확인
        if camera < route[0]:
            answer += 1
            # 카메라를 진출 지점으로 변경해줌
            camera = route[1]
    
    
    return answer