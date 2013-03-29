text = [line.strip() for line in open("../data/clusteredtags.txt")]

for line in text:
	print "\\item Does this sentence start with "+str(line)+"?"
