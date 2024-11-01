def solution(sequence, k):
    # 하나씩 넣었을 때 stack의 값이 k보다 작으면 append, 크면 pop후 append
    
#     def solution(sequence, k):
#     num = 0
#     for i in range(len(sequence)-1, -1, -1):
#         num += sequence[i]
#         if num > k:
#             num -= sequence.pop() 
#         if num == k:
#             while sequence[i-1] == sequence[-1] and i>0:
#                 i-=1
#                 sequence.pop()

#             return [i, len(sequence)-1]
    
    sum = 0
    for i in range(len(sequence)-1, -1, -1):
        sum += sequence[i]
        if sum > k :
            sum -= sequence.pop()
        if sum == k :
            while sequence[i-1] == sequence[-1] and i > 0:
                i -= 1
                sequence.pop()
            return [i,len(sequence)-1]
            
    
    


#     for i in range(len(sequence)-1, -1, -1):
#         idx2 = i
#         stack = 0
#         stack += sequence[i]
#         if stack == k :
#             return([idx2,idx2])
            
#         for j in range(i-1, -1, -1):
#             idx1 = j
#             stack += sequence[j]
#             if stack == k :
#                 return([idx1,idx2])
            
#             elif stack > k :
#                     break
                    
                     