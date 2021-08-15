def big_fibonacci(n):
    f1=1
    f2=1
    fnew=f2
    while len(str(fnew))<n:
        fnew=f1+f2
        f1=f2
        f2=fnew
    return fnew
