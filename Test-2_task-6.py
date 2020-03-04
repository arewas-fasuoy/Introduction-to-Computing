opn=['(','{','[']
clos=[')','}',']']
def test (str1):
    stack=[]
    pos=0
    for i in range(len(str1)):
        if (str1[i] in opn):
            stack.append(str1[i])
        elif (str1[i] in clos):
            pos=clos.index(str1[i])
            if len(stack)>0 and opn[pos]==stack[len(stack)-1]:
                stack.pop()
    if(len(stack) == 0):
        print('valid')
    else:
        print('InValid')
            
str1='({})'
test(str1)
