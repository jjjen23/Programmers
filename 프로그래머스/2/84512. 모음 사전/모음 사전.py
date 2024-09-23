from itertools import product

def solution(word):
    answer = 0

    dict = []
    words = ['A', 'E', 'I', 'O', 'U']
    for i in range(5): 
        for v in product(words, repeat = i+1):
            # 튜플형식으로 반환되기 때문에.. 이렇게 저장
            dict.append(''.join(v))
    dict.sort()
    
    answer = dict.index(word) + 1
    
    return answer