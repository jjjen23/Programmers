def solution(num_list):
    
    odd, even = 0, 0
    
    for i in range(len(num_list)):
        if i % 2 == 0:
            even += num_list[i]
        else:
            odd += num_list[i]
            
    if even >= odd:
        return even
    else:
        return odd
    
