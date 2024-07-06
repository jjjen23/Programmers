def solution(phone_number):
    phone_number = list(phone_number)
    # 마지막 네자리 전까지 * 로 교체
    for i in range(len(phone_number)-4):
       phone_number[i] = '*'
    
    
    answer = "".join(map(str,phone_number))
    return answer