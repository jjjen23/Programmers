import heapq

def solution(book_time):
    answer = 0
    book_time.sort()
    
    for time in book_time:
        #대실 시작 시간
        start_h,start_m = time[0].split(":")
        time[0] = int(start_h)*60 + int(start_m)
        #대실 종료 시간(10분을 미리 더해서 입실 가능시간으로 바꿈)
        end_h,end_m = time[1].split(":")
        time[1] = int(end_h)*60 + int(end_m) + 10
    # print(book_time)
    
    rooms = [] # 퇴실시간 저장(최소 힙으로 저장)
    
    for start, end in book_time:
        # 제일 빨리 퇴실하는 room과 가장 빠른 입실 시간을 비교
        # 힙이 존재하고(방이 있고) 퇴실 시각(최소값기준)보다 시작시간이 크거나 같다면 방빼. -> 그리고 그 방에 new 집어넣어
        if rooms and start >= rooms[0]:
            heapq.heappop(rooms)
        # 아니면? 새 방 배정받아(count 하는 경우) 
        else:
            answer += 1
        heapq.heappush(rooms, end)
    
        
    return answer