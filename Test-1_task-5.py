lst=[
{ ' roll_no ' : ' p19-1001 ' ,
' attendance ' : 88.4,
' marks ' : {
' english ' : (1.4, 2.5, 15, 9.6, 33),
' calculus ' : (2.4, 1.5, 12, 1.6, 21),
}
},
{ ' roll_no ' : ' p19-1002 ' ,
' attendance ' : 79.4,
' marks ' : {
' english ' : (2.4, 1.5, 12, 1.6, 21),
' DLD' : (2.4, 1.5, 12, 1.6, 21),
}
},
{ ' roll_no ' : ' p19-1003 ' ,
' attendance ' : 79.4,
' marks ' : {
' calculus ' : (2.4, 1.5, 12, None, 21),
' DLD' : (2.4, 1.5, 12, 1.6, 21)}
}
]
def dic(lst):
    mainDic = {}
    for dictionary in lst:
        dic = {}
        for i in dictionary:
            dictionary2=dictionary[i]
        for tpl in dictionary2:
            total = 0
            for k in dictionary2[tpl]:
                if(not k is None) :
                    total+=k
            dic[tpl] = total
        roll_no = dictionary[' roll_no ']
        mainDic[roll_no] = dic
    print(mainDic)
dic(lst)
