def solution(s):
    tem = []
    answer = ""
    abplist = s.split(" ")
    
    print(abplist)
    for i in abplist:
        tem.append(int(i))
    
    answer = str(min(tem)) +" "+ str(max(tem))
    
    return answer