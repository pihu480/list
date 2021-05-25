i=10
a=[]
b=[]
# c=[]
# d=[]
while i>0:
    num=int(input("enter a number"))
    if num%2==0:
        a.append(num)
    elif num%2!=0:
        b.append(num)
    i=i-1
print(a)
print(b)
# c=[]
# d=[]
# j=1
# while j>-9:
#     num1=int(input("enter the negetiv number"))
#     if num1== -0:
#         c.append(num)
#     j=j-1
# print(c)
# print(d)
