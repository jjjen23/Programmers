from collections import deque 
def solution(priorities, location):
    answer = 0
    # wanted = priorities[location]
    # print(wanted)
    indexlist = list(range(0,len(priorities)))
    #print(indexlist)
    indexlist = deque(indexlist)
    priorities = deque(priorities)
    cnt = 0
    while priorities:
        maxi = max(priorities)
        tem = priorities.popleft()
        idx = indexlist.popleft()
        
        if maxi == tem:
            cnt += 1
            if idx == location:
                return cnt
        else:
            priorities.append(tem)
            indexlist.append(idx)
    
    #return answer