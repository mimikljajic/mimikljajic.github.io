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

list1=[]
for i in range (10000,100000):
    if is_prime(i):
        istr=str(i)
        if istr[0]==istr[4] and istr[1]==istr[3]:
            list1.append(i)
print (list1)

