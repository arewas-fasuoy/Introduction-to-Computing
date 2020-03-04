dic={}
xlis = [i for i in range(11,21)]
ylis = [i for i in range(21,31)]
zlis = [i for i in range(31,41)]
dic['x'] = xlis
dic['y'] = ylis
dic['z'] = zlis
print (dic)
for lst in dic:
    v=dic[lst]
#    print (v)
    for i in range(len(dic)):
        x=v[4]
    print(x)
