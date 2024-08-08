# 정답 2 (집합을 이용해 중복 신고 제거) 
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    
    total = {}
    for name in id_list:
        total[name] = 0
    
    for re in set(report):
        name, who = re.split()
        total[who] += 1
    
    for re in set(report):
        name, who = re.split()
        if total[who] >= k:
            answer[id_list.index(name)] += 1
        
    return answer

"""
# 정답 1 (딕셔너리 안의 딕셔너리 구조) 

def solution(id_list, report, k):
    answer = []
    
    # 유저 별로 신고한 사람을 저장할 딕셔너리(사람 별, 중복신고 막기 위함)
    # 딕셔너리 안의 딕셔너리 구조로 자료구조 이용
    user_repo = {}
    # 유저 별 신고 총합 횟수 저장 딕셔너리
    total = {}
    
    for name in id_list:
        user_repo[name] = {} # 빈 딕셔너리 생성(딕셔너리 안의 빈 딕셔너리)
        total[name] = 0 # 0으로 초기화
    
    for re in report:
        name, who = re.split(" ")
        # 이용자 딕셔너리에 신고자의 키값이 없다면 카운트 반영됨
        if who not in user_repo[name]:
            total[who] += 1 
            user_repo[name][who] = True # 신고자 키 추가해주기
    
    
    report_name = []
    
    # K 번 이상 신고당하여 이용이 정지된 유저 리스트 만들어주기
    for name, value in total.items():
        if value >= k:
            report_name.append(name)
    
    # 이용자별로 신고한 사람중 이용이 정지된 사람이 있다면 카운트하여 정답 배열에 추가(= 유저가 받게될 메일의 수)
    for name in id_list:
        tem = 0
        for i in report_name:
            if i in user_repo[name]:
                tem +=1
        answer.append(tem)
        
    return answer

"""