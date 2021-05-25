list1=[2,3,1,4,5,9]
list2=[100,200,300,400,500,600]
i=0
while i<len(list1):
    i=i+1
    #print(list1[i])
    k=len(list2)-1
    while k>=0:
        k=k-1
        print(list1[i],list2[k])