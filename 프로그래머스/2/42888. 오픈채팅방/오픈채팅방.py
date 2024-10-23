def solution(record):
    answer = []
    dictid = {}
    
    for i in record:

        data = i.split(" ")
        if data[0] == "Leave":
            continue
        else:
            state, idd, nickname = data
            if idd not in dictid:

                dictid[idd] = nickname
            else:
                dictid[idd] = nickname
                
    # print(dictid)
    
    for i in record:
        data = i.split(" ")
        if data[0] == "Enter":
            answer.append(f'{dictid[data[1]]}님이 들어왔습니다.')
        elif data[0] == "Leave":
            answer.append(f'{dictid[data[1]]}님이 나갔습니다.')
        
    
    return answer