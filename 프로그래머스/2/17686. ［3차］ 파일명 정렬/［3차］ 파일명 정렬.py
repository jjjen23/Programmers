import re

def solution(files):
    answer = []
    dict1={}
    
    #head : 숫자 전
    #number : 숫자
    #tail : 숫자 이후
    for i in range(len(files)):
        match = re.split(r'(\d+)', files[i], maxsplit=1)
        if len(match) == 3:
            dict1[i] = (match[0],match[1],match[2])
        else:
            dict1[i] = (match[0],match[1])
    
    # print(dict1)
    
    #dict1.items()는 딕셔너리의  (key,value)쌍을 튜플 리스트로 변환한다.
    # 정렬순서 : head(오름차순,대소문자x) -> number(숫자 오름차순)
    # 둘 다 같다면 원래 입력에 주어진 순서를 유지(원래키값)
    dict1 = dict(sorted(dict1.items(), key=lambda item : (item[1][0].lower(),int(item[1][1]),item[0])))
    
    # print(dict1)
    
    for item in dict1.values():
        tem = ''.join(item)
        answer.append(tem)

    
    
    return answer