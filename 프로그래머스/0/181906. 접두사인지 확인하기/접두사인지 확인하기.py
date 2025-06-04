def solution(my_string, is_prefix):

    idx = len(is_prefix)
    if my_string[:idx] == is_prefix:
        return 1
    else:
        return 0
    
