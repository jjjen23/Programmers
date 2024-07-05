def solution(n):
    tem_set = set()
    for i in range(1, int(n ** 0.5)+1):
        if n % i == 0 :
            tem_set.add(i)
            tem_set.add(n//i)
        
    answer = sum(tem_set)
    return answer