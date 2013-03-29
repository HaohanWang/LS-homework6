text = [line.strip() for line in open("../data/resultB.txt")]

t=text[0][2:-42]

m=t.split("), (")

a=[]

for item in m:
	b=item.split(",")
	a.append((int(b[0]), float(b[1])))

sta=sorted(a, key=lambda tup:tup[0])

#print text

#print m
c1=0.0
c2=0.0
c3=0.0
c4=0.0
c5=0.0
c6=0.0


for i in range(len(sta)):
	if i<=6:
		c1+=sta[i][1]
	elif i<=21:
		c2+=sta[i][1]
	elif i<=36:
		c3+=sta[i][1]
	elif i<=261:
		c4+=sta[i][1]
	elif i<=295:
		c5+=sta[i][1]
	else:
		c6+=sta[i][1]
	
print c1/6.0
print c2/15.0
print c3/15.0
print c4/225.0
print c5/34.0
print c6/209.0	
	
