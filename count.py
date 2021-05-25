a = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
count=0
sum=0
while i<len(a):
    if a[i]%2==0:
        print("even")
    elif a[i]%2!=0:
        print("odd")
        count=count+(a[i])
        sum=sum+(a[i])
    i=i+1
print(count)
print(sum)
print(sum//i)

