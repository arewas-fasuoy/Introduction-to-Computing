#combining data from two files
import os
directory="res"
name="file.txt"
name2="file2.txt"
filename=os.path.join(directory,name)
#print (filename)
l=[]
f = open(filename,'r')

for line in f:
    l.append(line.strip())

f.close()
filename2=os.path.join(directory,name2)
#print (filename2)
l2=[]
y = open(filename2,'r')

for line in y:
    l2.append(line.strip())

y.close()
for i in range(len(l)):
    print(l[i] +' '+ l2[i])
