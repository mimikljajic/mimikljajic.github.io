def to_hex(n):
    list1=["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
    x=n//16
    y=n%16
    if x>0:
        result=list1[x]+list1[y]
    else:
        result=list1[y]
    return result

def hex_code(x,y,z):
    if len(to_hex(x))==1:
        xnew="0"+to_hex(x)
    else:
        xnew=to_hex(x)
    if len(to_hex(y))==1:
        ynew="0"+to_hex(y)
    else:
        ynew=to_hex(y)
    if len(to_hex(z))==1:
        znew="0"+to_hex(z)
    else:
        znew=to_hex(z)
    return "#"+xnew+ynew+znew