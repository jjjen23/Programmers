def solution(x):
    answer = True
    list_x = list(str(x))
    h = 0
    for i in list_x:
        h+= int(i)
    if x % h != 0:
        answer = False
    return answer