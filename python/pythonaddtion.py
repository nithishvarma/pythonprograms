a=[]
b=[]
c=[]
t=int(input('enter no of rows and columns'))
print('enter elements in a')
for i in range(t):
	s=[]
	j=0
	for j in range(t):
		s.append(int(input()))
	a.append(s)
print('enter elements in b')
for i in range(t):
	s=[]
	j=0
	for j in range(t):
		s.append(int(input()))
	b.append(s)
for i in range(t):
	s=[]
	j=0
	for j in range(t):
		s.append(a[i][j]+b[i][j])
	c.append(s)
print(c)




