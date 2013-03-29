text = [line.strip() for line in open("../data/informative.txt")]

for line in text:
	print line+"\\\\"
