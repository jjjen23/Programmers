possible = ["-","_","."]

def solution(new_id):
    answer = ''
    
    
    # 1단계
    new_id = new_id.lower()
    
    
    # 2단계
    for i in new_id:
        if i.isalpha() or i in possible or i.isdigit():
            answer += i
    
    # 3단계
    while ".." in answer:
        answer = answer.replace("..",".")
    
    answer = list(answer)
    
    # 4단계
    if answer and answer[0] == '.':
        del answer[0]
        
    if answer and answer[-1] == '.':
        del answer[-1]
    
    # 5단계
    if not answer:
        answer = ["a"]
    
    # 6단계
    if len(answer) > 15 :
        answer = answer[:15]
    if answer[-1] == ".":
        del answer[-1]
        
    # 7단계
    if len(answer) < 3 :
        last = answer[-1]
        while len(answer) < 3:
            answer.append(last)
        
    answer = "".join(map(str,answer))
    return answer