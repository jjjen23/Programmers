def solution(numbers):
    answer = ''
    
    if len(numbers) == numbers.count(0):
        return '0'
    sorted_num = sorted(numbers, key = lambda x : str(x) * 4, reverse=True)
    # print(sorted_num)
    
    for i in sorted_num:
        answer += str(i)
    
#     dict1 = {}
#     maxlen = 0
#     for i in numbers :
#         if len(str(i)) > maxlen:
#             maxlen = len(str(i))
#     # 그냥 맥스값 찾아서 len구해도 똑같아..

#     for i in numbers:
#         dict1[i] = str(i).ljust(maxlen,'0')
#     print(dict1)
    
#     newdict1 = dict(sorted(dict1.items(), key = lambda x : -int(x[1])))
#     print(newdict1)
    
#     for item in newdict1.items():
#         answer += str(item[0])
        
    
    
    return answer