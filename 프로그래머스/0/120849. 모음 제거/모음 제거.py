def solution(my_string):

    list_s = ['a','e','i','o','u']
    
    for i in list_s:
        my_string = my_string.replace(i,"")

    
    return my_string