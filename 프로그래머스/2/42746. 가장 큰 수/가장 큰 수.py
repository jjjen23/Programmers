def solution(numbers):
    answer = ''
    
    if len(numbers) == numbers.count(0):
        return '0'
    
    sorted_num = sorted(numbers, key = lambda x : str(x) * 4, reverse=True)
    # print(sorted_num)
    
    for i in sorted_num:
        answer += str(i)

#     dict1 = {}
#     for num in numbers:
#         dict1[num] = (str(num)*4) # 1000자리 수 까지 확장해서, 비교.  
    
#     dict1 = dict(sorted(dict1.items(), key= lambda x: x[1], reverse = True))
    
#     # print(dict1)
    
#     for item in dict1.items():
#         answer+=str(item[0])
#     # print(answer)    
    
    return answer