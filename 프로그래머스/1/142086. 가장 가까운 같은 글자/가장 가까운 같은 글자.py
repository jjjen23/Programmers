def solution(s):
    answer = []
    dict = {}
    
    for i in range(len(s)):
        # 처음 나오는 알파벳은 정답 리스트에 -1추가하고, 사전에 인덱스 번호 등록하기
        if s[i] not in dict:
            answer.append(-1)
            dict[s[i]] = i
        # 처음 나오는 알파벳이 아니라면 정답리스트에 (현재 인덱스 번호 - 사전에 저장했던 인덱스번호)추가해주고 현재 인덱스 번호로 갱신해주기     
        else:
            answer.append(i - dict[s[i]])
            dict[s[i]] = i
    return answer

# solution("banana")