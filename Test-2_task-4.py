lst=[-25, -10, -7, -3, 2, 4, 8, 10]
ans=[0,0,0]
for i in range(len(lst)):
    ans[0]=lst[i]
    for j in range(i+1,len(lst)):
        ans[1]=lst[j]
        for k in range(j+1,len(lst)):
            ans[2]=lst[k]
            if (sum(ans)==0):
                print(ans)
