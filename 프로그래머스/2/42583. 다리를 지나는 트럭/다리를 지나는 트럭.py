from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    truck_weights = deque(truck_weights)
    
    onBridge = deque() 
    endTruck = 0
    cntTruck = len(truck_weights)
    
    time = 0
    
    #트럭이 전부 통과 할 때 까지
    while endTruck < cntTruck:
        
        time += 1
        
        # 첫번째 트럭만 확인해주면 됨, 첫번째 트럭이 다리를 전부 통과할 때 -> 통과한 트럭수 증가시켜줌
        if onBridge and onBridge[0][1] == bridge_length:
                onBridge.popleft()
                endTruck += 1
        
        # 트럭을 올렸을 때, 조건에 부합하다면 -> 다리 위로 올려준다.
        if truck_weights and sum(truck[0] for truck in onBridge) + truck_weights[0]  <= weight and len(onBridge) + 1 <= bridge_length:
            
            onBridge.append([truck_weights.popleft(),0])
        
        # 올려진 트럭에 대해 매 반복 마다 1초씩 증가.
        for i in range(len(onBridge)):
            onBridge[i][1] += 1
            
            
        
        
            
    answer = time
    
    return answer