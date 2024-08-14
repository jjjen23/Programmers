def solution(s):
    tem = []
    answer = []
    abplist = s.split(" ")
    
    print(abplist)
    for i in abplist:
        tem.append(int(i))
    
    answer.append(min(tem))
    answer.append(max(tem))
    
    st = ' '.join(map(str,answer))
    
    return st