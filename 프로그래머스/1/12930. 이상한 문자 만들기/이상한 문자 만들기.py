#ord(문자->유니코드숫자)함수와 chr(숫자->문자)함수

def solution(s):
    answer_list = []
    words = s.split(" ")
    
    for word in words:
        tem_ans = ''
        for i in range(len(word)):
            if i % 2 == 0:
                tem_ans += word[i].upper()
            else:
                tem_ans += word[i].lower()
        answer_list.append(tem_ans)
        #print(answer_list)
        
    #print(' '.join(answer_list))        
    return ' '.join(answer_list)

