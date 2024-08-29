def solution(arr1, arr2):
    
    
    answer = []
    for k1 in range(len(arr1)):
        temlist = []
        for k2 in range(len(arr2[0])):
            tem = 0
            for i in range(len(arr1[0])):
                tem += arr1[k1][i] * arr2[i][k2]
            temlist.append(tem)
        answer.append(temlist)        
        
    return answer