def solution(a, b, c):
    # answer = 0
    
    # 모두 다를때 
    # 두 숫자가 같을때
    # 세 숫자가 같을때
    # 집합이용
    case1 = (a+b+c)
    case2 = ((a**2) + (b**2) + (c**2))
    case3 = ((a**3) + (b**3) + (c**3))

    testSet = set([a,b,c])
    
    if len(testSet) == 3:
        return case1
    elif len(testSet) == 2:
        return case1 * case2
    elif len(testSet) == 1:
        return case1 * case2 * case3
    
