t=int(input())
a=[]
for i in range(t):
    b=[]
    for j in range(t):
        b.append(int(input()))
    a.append(b)
print(a)
c,e,d=0
for i in range(t):
    c+=a[i][i]
    if i<t-1:
        d+=a[i][i+1]
    if i>0:
        e+=a[i][i-1]
print(c+d+e)

    
            
    
