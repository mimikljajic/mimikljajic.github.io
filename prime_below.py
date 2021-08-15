def is_prime(n):
    i=1
    nodiv=0
    while i<=n:
        if n%i==0:
            nodiv+=1
        i+=1
    if nodiv==2:
        return True
    else:
        return False


def prime_below(n):
    listprime=[]
    if n<=1:
        return False
    for i in range (2,n):
        if is_prime(i):
            listprime.append(i)
    return(listprime)