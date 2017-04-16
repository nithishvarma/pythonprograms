
from __future__ import print_function
def p():
    a=raw_input('enter the sentence ')
    b=''
    c=[]
    i=0
    while i<len(a):
        if a[i]=='.':
            c.append(b)
            b=''
        else:
            b=b+a[i]
        i=i+1
    c.append(b)
    c.reverse()
    for i in c:
        print(i,end=' ')
t=input()
for i in range(t):
    p()


    
