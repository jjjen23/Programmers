def solution(str1, str2):
    answer = 0
    
    str11 = []
    str22 = []
    
    for i in range(0,len(str1)-1):
        if str1[i:i+2].isalpha():
            tem = str1[i:i+2].lower()
            str11.append(tem)
            
    for i in range(0,len(str2)-1):
        if str2[i:i+2].isalpha():
            tem = str2[i:i+2].lower()
            str22.append(tem)
            
    # print(str11)
    # print(str22)
    
    if len(str11) == 0 and len(str22) == 0:
        return 65536
    
    set1 = set(str11)
    set2 = set(str22)
    
    
    interlist = []
    unionlist = []
    
    for i in set1 & set2:
        n = min(str11.count(i), str22.count(i))
        interlist += [i] * n
    
    for i in set1 | set2:
        n = max(str11.count(i), str22.count(i))
        unionlist += [i] * n
        
    # print(interlist)
    # print(unionlist)
    
    
    answer = int((len(interlist) / len(unionlist)) * 65536) 
    
    return answer
