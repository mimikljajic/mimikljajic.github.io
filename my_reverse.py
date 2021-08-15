def my_reverse(list1):
    list2=[]
    x=len(list1)-1
    while x>=0:
        list2.append(list1[x])
        x-=1
    return list2
