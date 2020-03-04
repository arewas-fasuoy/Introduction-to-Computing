#finding index of numbers whose sum is equal to a target
def summ(lst,target):
    for i in range(len(lst)):
        for j in range(1,len(lst)):
            if (lst[i]+lst[j])==target:
                return i,j

v=[10,20,10,30,50,60,70]
target=input("Enter the target: ")
print(summ(v,int(target)))
