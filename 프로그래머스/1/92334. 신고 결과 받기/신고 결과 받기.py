def solution(id_list, report, k):
    answer = []
    
    user_repo = {}
    total = {}
    
    for name in id_list:
        user_repo[name] = {}
        total[name] = 0
    
    for re in report:
        name, who = re.split(" ")
        if who not in user_repo[name]:
            total[who] += 1
            user_repo[name][who] = True
    
    
    report_name = []
    
    for name, value in total.items():
        if value >= k:
            report_name.append(name)
    
    
    for name in id_list:
        tem = 0
        for i in report_name:
            if i in user_repo[name]:
                tem +=1
        answer.append(tem)
        
    return answer