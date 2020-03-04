#sorting counter by value in descending order
dic={'Math':81,'English':76, 'Physics':83, 'Chemistry':87}
lst=dic.items()
a=[]
def counter(lst):
    for k in lst:
#        print (k)
        a.append(k)
#    print (a)
    for i in range(len(a)):
#        print(i)
        for j in range(len(a)-1):
            if a[j][1]>a[j+1][1]:
                position = a[j]
                a[j]= a[j + 1]  
                a[j + 1]= position
    a.reverse()
    return a
    
print(counter(lst))
#print (type(lst))"
