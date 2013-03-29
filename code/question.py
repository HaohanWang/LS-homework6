import sys

def mapFromWordtoList(w):
	if w.find("cluster")!=-1:
		if w[0]=="J":
			return ["JJ","JJR","JJS"]
		elif w[0]=="N":
			return ["NN","NNP","NNPS","NNS","PRP","PRP$"]
		elif w[0]=="R":
			return ["RB","RBR"]
		elif w[0]=="V":
			return ["VB","VBD","VBG","VBN","VBP","VBZ"]
		elif w[0]=="W":
			return ["WDT","WP","WRB"]
	else:
		return [w]

def specificQuestion(i, sent):
	if i==1:
		return len(sent)==0
	elif i==2: #if the question is singular
		S = ["NN", "NNP", "VBP","VBZ"]
		for j in range(len(S)):
			for k in range(len(sent)):
				if S[j]==sent[k]:
					return True
		return False
	elif i==3: #if the question is plural
		S = ["NNS", "NNPS"]
		for j in range(len(S)):
                        for k in range(len(sent)):
                                if S[j]==sent[k]:
                                        return True
                return False
	elif i==4: #if the question contains a comparative word
		S = ["JJR", "RBR"]
		for j in range(len(S)):
                        for k in range(len(sent)):
                                if S[j]==sent[k]:
                                        return True
                return False
	elif i==5: #if the question contains a superlative word
		S = ["JJS", "RBS"]
		for j in range(len(S)):
                        for k in range(len(sent)):
                                if S[j]==sent[k]:
                                        return True
                return False
	elif i==6: #if there is an unmatched bracket
		if "(" in sent and ")"not in sent:
			return True
		else:
			return False
		
def startWith(b, sent):
	if len(sent)==0:
		return False
	else:
		if sent[0]==b:
			return True
		else:
			return False

def biGram(n, sent):
	if len(sent)==0:
		return True
	m=mapFromWordtoList(n)
	for i in range(len(m)):
		if sent[-1]==m:
			return True
	return False

def triGram(nt1, nt2, sent):
	t1=mapFromWordtoList(nt1)
	t2=mapFromWordtoList(nt2)
	if len(sent)<=1:
		return biGram(nt2, sent)
	else:
		for i in range(len(t1)):
			for j in range(len(t2)):
				if sent[-1]==t2[j] and sent[-2]==t1[i]:
					return True
		return False

def existOne(n, sent):
	m=mapFromWordtoList(n)
	for i in range(len(sent)):
		for j in range(len(m)):
			if sent[i]==m[j]:
				return True
	return False

def existTwo(t1, t2, sent):
	return existOne(t1, sent) and existOne(t2, sent)

def existThree(t1, t2, t3, sent):
	return existOne(t1, sent) and existOne(t2, sent) and existOne(t3, sent)

def askQuestion(i, word, sent):
	if i<=6:
		return specificQuestion(i, sent)
	elif i<=21:
		return startWith(word, sent)
	elif i<=36:
		return biGram(word, sent)
	elif i<=261:
		w=word.split()
		return triGram(w[0], w[1], sent)
	elif i<=295:
		return existOne(word, sent)
	else:
		w=word.split()
		return existTwo(w[0], w[1], sent)
#	else:
#		w=word.split()
#		return existThree(w[0], w[1], w[2], sent)

def checkQuestion(i):
	dic=getDic()
#	print dic
	if i <=1:
		return True
	if i in dic:
#		print "zaiazaia"
		return True
	else:
#		print "buzaibuzai"
		return False
def getDic():
	question=[line.strip() for line in open("../data/question.txt")]
	dic={}
	for line in question:
		i = line.find(" ") 	
		dic[int(line[:i])]=line[i+1:]
	return dic

text1=[line.strip() for line in open("../data/tags.txt")]
text2=[line.strip() for line in open("../data/clusteredtags.txt")]
order=7
for line in text2:
	print str(order)+" "+str(line)
	order+=1	
#order=101
for line in text2:
	print str(order)+" "+str(line)
	order+=1
for i in range(len(text2)):
	for j in range(len(text2)):
		print str(order)+" "+str(text2[i])+" "+str(text2[j])
		order+=1
#order=351
for line in text1:
	print str(order)+" "+str(line)
	order+=1
#order=381
for i in range(len(text2)):
	for j in range(len(text2)):
		if i!=j:
			print str(order)+" "+str(text2[i])+" "+str(text2[j])
			order+=1
#order=701
#for i in range(len(text2)):
#	for j in range(len(text2)):
#		for k in range(len(text2)):
#			if i!=j and j!=k and i!=k:
#				print str(order)+" "+str(text2[i])+" "+str(text2[j])+" "+str(text2[k])
#				order+=1
