 
a = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
while i<len(a):
    #num=int(input("enter tha number"))
    if a[i]%2==0:
        print("even")
        #a.append(num)
    elif a[i]%2!=0:
        #a.append(num)
        print("odd")
    i=i+1
print(a)

