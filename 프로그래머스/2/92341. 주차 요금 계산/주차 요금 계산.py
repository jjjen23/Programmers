from math import ceil

def solution(fees, records):
    answer = []
    
    dict1 = {}
    
    for record in records:
        a,b,c = record.split()
        if b not in dict1:
            dict1[b] = [a]
        else:
            dict1[b].append(a)
    
    for x in dict1.values():
        if len(x) % 2 != 0:
            x.append("23:59")

    
    totaltime = []
    
    for key,val in dict1.items():
        total = 0
        for i in range(len(val)):
            hh,mm = val[i].split(':')
            hh,mm = int(hh),int(mm)
            if i % 2 == 0:
                total += -((hh*60) + mm)
            else:
                total += ((hh*60) + mm)
        totaltime.append((key,total))
                
    # print(totaltime)
    totaltime=sorted(totaltime, key = lambda x : x[0])
    print(totaltime)
    
    for time in totaltime:
        if fees[0] < time[1]:
            temfee = fees[1]+ceil((time[1]-fees[0])/fees[2]) * fees[3]
            answer.append(temfee)
        else:
            answer.append(fees[1])
    
    return answer