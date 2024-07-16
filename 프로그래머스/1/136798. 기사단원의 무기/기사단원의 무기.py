def solution(number, limit, power):
    
    gisadanList = []
    
    for i in range(1, number+1):
        temSum = set()
        for j in range(1,int(i**0.5)+1):
            if i % j == 0:
                temSum.add(j)
                temSum.add(i//j)
        gisadanList.append(len(temSum))
    
    for i in range(len(gisadanList)):
        if  gisadanList[i] > limit:
            gisadanList[i] = power
    
    answer = sum(gisadanList)
    
    return answer