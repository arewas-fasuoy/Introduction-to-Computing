#code for calculating square root
def abs(x):
    if x>0:
        return x
    elif x==0:
        return 0
    else:
        return -x
def average(a,b):
    avg=(a+b)/2.0
    return avg
def good_enough(gues,x):
    if abs(gues*gues-x)<0.00001:
        return True
    else:
        return False
def improve_gues(gues,x):
    avg=average(gues,x/gues)
    return avg
def sqrt(x,gues=0.1):
    if x==0:
        return None
    if good_enough(gues,x):
        return gues
    else:
        new_gues=improve_gues(gues,x)
        return sqrt(x,new_gues)
v=sqrt(36)
print ("the squaroot is",v)
