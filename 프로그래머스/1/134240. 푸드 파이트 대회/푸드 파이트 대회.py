def solution(food):
    answer = ''
    right = ''
    for i in range(1,len(food)):
        tem = int(food[i] // 2)
        right += str(i) * tem
    
    left = right[::-1]
    answer+=right+'0'+left

            
    return answer