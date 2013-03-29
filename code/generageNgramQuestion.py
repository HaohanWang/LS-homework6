text = [line.strip() for line in open("../data/clusteredtags.txt")]
tag=[]
for line in text:
	tag.append(line)
for i in range(len(tag)):
	print "\\item Is the former tag "+str(tag[i])+"?"
for i in range(len(tag)):
	for j in range(len(tag)):
		 print "\\item Are the former two tags "+str(tag[i])+" and "+str(tag[j])+"?"
#for i in range(len(tag)):
#	for j in range(len(tag)):
#		for k in range(len(tag)):
#			print "\\item Are the former three tags "+str(tag[i])+", "+str(tag[j])+" and "+str(tag[k])+"?"
