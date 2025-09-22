def solution(s):
    answer = 0
    
    # 문자가 연속해서 반복되는 만큼 숫자로 압축해서 표현, 1은 생략
    # 연속되는 단위는 조절가능 -> 단어로 압축하는 개념
    # 1개 이상 단위로 문자열을 잘라 압축하여 표현한 문자열중 가장 짧은 것의 길이를 반환하도록
    
    if len(s) == 1:
        return 1
    
    resset = set()
    
    for i in range(1,len(s)):
        prev = ''
        temstr = ''
        cnt = 1
        
        for j in range(0,len(s),i):
            if prev == ''.join(s[j:j+i]):
                cnt += 1
            else:
                if cnt > 1:
                    temstr += (str(cnt) + prev)
                    cnt = 1
                else:
                    temstr += prev
            prev = ''.join(s[j:j+i])
            # cnt = 1
        if cnt > 1:
            temstr += (str(cnt)+prev)
        else:
            temstr += prev
        resset.add(len(temstr))
    
    answer = min(resset)
    

    return answer


"""
def solution(s):
    if len(s) == 1:
        return 1
    
    resset = set()
    answer = 0
    # print(len(s))
    # print(test[0:4])
    
    for i in range(1,len(s)):
        # dict1 = {}
        strtem = ''
        prev = ''
        cnt = 1
        
        for j in range(0,len(s),i):
            # 슬라이싱 문자값이 이전과 같다면 cnt ++
            # 다르다면 이전 문자와 cnt수를 strtem에 + ->cnt 초기화
            chgstr = ''.join(s[j:j+i])
            
            if chgstr == prev:
                cnt +=1
            # 값이 다를때!!
            else:
                # prev 값이 있다면~
                if prev:
                    # 중복됐다면 중복 값과 이전글자 추가, cnt초기화
                    if cnt > 1:
                        strtem += str(cnt)+prev
                        cnt = 1
                    # 중복된 적 없다면 이전 글자만 추가
                    else:
                        strtem += prev
                # 상태 없데이트(prev값이 있든 없든 매 반복 공통작업)
                prev = chgstr
                # cnt = 1
        
        # 마지막 남는 문자열 처리
        if cnt > 1:
            strtem += str(cnt)+prev
        else:
            strtem += prev
        # print(strtem)
        resset.add(len(strtem))
        
    resset = list(resset)
    resset.sort()
    answer =resset[0]
        
    return answer
"""





        # resset.add(len(strtem))
            
            # chgstr = ''.join(s[j:j+i])
            # # print(chgstr)
            # if chgstr in dict1:
            #     dict1[chgstr] += 1
            # else:
            #     dict1[chgstr] = 1
                
        # for k,v in dict1.items():
        #     if v == 1:
        #         strtem+=str(k)
        #     else:
        #         strtem+=str(v)
        #         strtem+=k
        # print(strtem)
        
    # resset = list(resset)
    # resset.sort()
    # print(resset)
    # answer = resset[0]