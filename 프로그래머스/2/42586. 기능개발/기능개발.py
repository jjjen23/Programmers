import math

def solution(progresses, speeds):
    answer = []
    nameunday = []
    
    #print(math.ceil(3.5))
    
    for i in range(len(progresses)):
        tem = math.ceil((100 - progresses[i]) / speeds[i])
        nameunday.append(tem)
    
    #print(nameunday)
    
    # while len(nameunday):
    #     tem = 1
    #     wait = nameunday.pop(0)
    #     for i in range(len(nameunday)):
    #         if wait >= nameunday[i]:
    #             tem += 1
    #         else:
    #             print(i)
    #             answer.append(tem)
    #             del nameunday[0:i]
    #             break
    

    while len(nameunday):
        m = nameunday.pop(0)
        tem = 1
        
        while nameunday and m >= nameunday[0]:
            nameunday.pop(0)
            tem += 1
        
        answer.append(tem)
    
        
    return answer