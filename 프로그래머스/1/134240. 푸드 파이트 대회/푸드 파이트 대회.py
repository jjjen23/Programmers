def solution(food):
    answer = ''
    tem_list = []
    for i in range(1,len(food)):
        tem = int(food[i] // 2)
        for j in range(tem):
            tem_list.append(i)
    
    left = ''.join(map(str,tem_list))
    tem_list.sort(reverse=True)
    right = ''.join(map(str,tem_list))
    
    answer = left + '0' + right
            
    return answer