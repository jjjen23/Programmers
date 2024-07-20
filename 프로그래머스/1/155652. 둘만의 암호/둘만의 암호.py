apb = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def solution(s, skip, index):
    answer = ''
    
    # 알파벳 리스트에서 skip에 든 문자 제거해주기
    for i in skip:
        apb.remove(i)
    
    # 제거된 알파벳 길이 저장
    n = len(apb)
    
    # index 만큼 뒤의 알파벳으로 바꿔줌, 알파벳 길이만큼 인덱스에 나머지 취해주기 
    for i in s:
        # 현재 인덱스 반환
        index_i = apb.index(i)
        # index만큼 뒤에 인덱스로 변환한 문자 정답에 추가하기
        answer += apb[(index_i+index)%n]
    
    
    return answer