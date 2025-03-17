def solution(my_string):
    answer = ''
    my_string = my_string.lower()
    lists = list(my_string)
    lists.sort()
    answer = ''.join(lists)
    
    return answer