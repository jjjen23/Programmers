possible = ["-","_","."]

def solution(new_id):
    answer = ''
    new_id = list(new_id)
    
    # 1단계
    for i in range(len(new_id)):
        if new_id[i].isupper():
            new_id[i] = new_id[i].lower()
    
    # 2단계
    for i in range(len(new_id)):
        if new_id[i].isalpha() or new_id[i] in possible or new_id[i].isdigit():
            answer += new_id[i]
    
    #new_id =  str(new_id)
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