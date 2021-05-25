a=["m","i","s","s","i","s","s","p","i","i"] 
b=[] 
i=0
while i<len(a):
    count=0
    j=0
    while j<len(a):
        if a[j]==a[i]:
            count+=1
        j+=1
    if a[i] in b:
        i+=1
        continue
    b.append(a[i])
    print (a[i],"",count)
    i+=1
print (b)