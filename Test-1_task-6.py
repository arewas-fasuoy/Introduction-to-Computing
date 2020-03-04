#finding largest element in a each row of list
l=[(23,5,6,15,18),(4,16,24,67,10),(12,54,23,76,11)]
def largest_element(l):
    k=0
    for i in l:
        k+=1
        large = i[0]
        for j in i: 
            if large<j: 
                large=j
        print("the large element in row",k,'=',large)
    
        
largest_element(l)
