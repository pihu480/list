num=0
kum=0
sum=0
aa=0
x=[]
y=[]
z=[]
hum=0
tum=0
pum=0
g=[]
a=[
    [0,1,1],
    [1,1,1],
    [1,1,1],
]
n=0
u=2
for i in a:
    for l in range(1):
        num+=i[aa]
    for k in range(1):
        kum+=i[1]
    for h in range(1):
        hum+=i[2]
    for d in range(1):
        tum+=i[n]
    n+=1
    for oo in range(1):
        pum+=i[u]
    u-=1
    for j in range (len(i)):
        sum+=(i[j])
        if j==(len(i)-1):
            x.append(sum)
            sum=0
if num==pum==kum==tum==hum:
    print("magic square")
else:
    print("not magic square")
#print