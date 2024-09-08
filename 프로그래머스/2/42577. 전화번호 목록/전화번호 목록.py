def solution(phone_book):
    answer = True
    
    # 사전순 정렬하면 접두사가 인접한 순으로 정리됨(정렬 법칙이 그래)
    phone_book.sort()
    # print(phone_book)
    
    for i in range(0,len(phone_book)-1):
        if phone_book[i+1][0:len(phone_book[i])] == phone_book[i] or phone_book[i][0:len(phone_book[i+1])] == phone_book[i+1]:
            answer = False
            break
                
    return answer