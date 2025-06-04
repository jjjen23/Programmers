def solution(num_list):

    # 마지막원소 > 이전 원소 -> append(마지막원소-이전원소)
    # else: append(2*마지막원소)
    if num_list[-1] > num_list[-2]:
        num_list.append(num_list[-1]-num_list[-2])
    else:
        num_list.append(num_list[-1]*2)
    return num_list