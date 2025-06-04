def solution(binomial):

    if '+' in binomial:
        a,b = binomial.split(' + ')
        return (int(a) + int(b))
    elif '-' in binomial:
        a,b = binomial.split(' - ')
        return (int(a) - int(b))
    elif '*' in binomial:
        a,b = binomial.split(' * ')
        return (int(a) * int(b))