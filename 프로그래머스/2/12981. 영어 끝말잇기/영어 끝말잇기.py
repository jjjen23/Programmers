def solution(n, words):
    answer = []
    #wordslen = len(words)
    people = {}
    # 딕셔너리에 사람과 현재 차례 저장
    for i in range(n):
        people[i] = 0
    
    #print(words[-1][-1])
    
    # 정답으로 나왔던 애들 저장해둘 리스트
    a_list = []
    
    for i in range(0, len(words)):
        # 사람 별 차례 갱신해주기
        people[i % n] += 1
        #print(i)
        tem = words[i]
        
        if len(a_list) > 0:
            # --- 실패 조건 두 가지 -----
            # 이미 말한 단어를 말했을 때
            if tem in a_list:
                answer.append((i % n) +1) # 번호 추가
                answer.append(people[(i % n)]) # 차례 추가
                break

            # 끝말잇기 실패 시
            if a_list[-1][-1] != tem[0]:
                answer.append((i % n) +1) # 번호 추가
                answer.append(people[(i % n)]) # 차례 추가
                break
        
        a_list.append(tem)
        
    if len(answer) == 0:
        answer.append(0)
        answer.append(0)
    
    return answer

"""
# 정답1 : pop으로 풀기

def solution(n, words):
    answer = []
    wordslen = len(words)
    people = {}
    # 딕셔너리에 사람과 현재 차례 저장
    for i in range(n):
        people[i] = 0
    
    #print(words[-1][-1])
    
    # 정답으로 나왔던 애들 저장해둘 리스트
    a_list = [words.pop(0)]
    people[0] += 1 
    
    for i in range(1, wordslen):
        # 사람 별 차례 갱신해주기
        people[i % n] += 1
        #print(i)
        tem = words.pop(0)
        # --- 실패 조건 -----
        # 이미 말한 단어를 말했을 때
        if tem in a_list:
            answer.append((i % n) +1) # 번호 추가
            answer.append(people[(i % n)]) # 차례 추가
            break
            
        # 끝말잇기 실패 시
        if a_list[-1][-1] != tem[0]:
            answer.append((i % n) +1) # 번호 추가
            answer.append(people[(i % n)]) # 차례 추가
            break
        
        
        a_list.append(tem)
    if len(answer) == 0:
        answer.append(0)
        answer.append(0)
    
    return answer
"""