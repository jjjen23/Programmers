def solution(numbers):
    answer = ''
    
    if len(numbers) == numbers.count(0):
        return '0'
    
    sorted_num = sorted(numbers, key = lambda x : str(x) * 4, reverse=True)
    # print(sorted_num)
    
    for i in sorted_num:
        answer += str(i)

# 미스테리 미스테리.. 오.. 왜 아래는 안돼.. -> 딕셔너리는 똑같은 값에 대해 처리불가능..!!!! ex)[0, 1000, 0, 0]의 입력의 경우, 1000000가 아니라, 10000가 나옴
#     dict1 = {}
#     for num in numbers:
#         dict1[num] = (str(num)*4) # 1000자리 수 까지 확장해서, 비교.  
    
#     dict2 = dict(sorted(dict1.items(), key= lambda x: x[1], reverse = True))
    
#     # print(dict2)
    
#     for item in dict2.items():
#         answer+=str(item[0])
#     # print(answer)    
    
    return answer