text1 = [line.strip() for line in open("../data/tags.txt")]
text2 = [line.strip() for line in open("../data/clusteredtags.txt")]

tag1=[]
tag2=[]

for line in text1:
	tag1.append(line)
for line in text2:
	tag2.append(line)

for i in range(len(tag1)):
	print "\\item Does this sentence contains "+str(tag1[i])+"?"
for i in range(len(tag2)):
	for j in range(len(tag2)):
		if i!=j:
			print "\\item Does this sentence contains "+str(tag2[i])+" and "+str(tag2[j])+"?"
