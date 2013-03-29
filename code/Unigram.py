import math
def log2(a):
	if a==0:
		return 0
	else:
		return math.log(a, 2)

def initializeDict():
	dic={}
	text = [line.strip() for line in open("../data/tags.txt")]
	for line in text:
		dic[line]=0
	return dic

def normalize(dic):
	s=0.0
	for item in dic:
		s+=dic[item]
	for item in dic:
		dic[item]=float(dic[item])/s
	return dic

def getDict(a):
	dic=initializeDict()
	text = [line.strip() for line in open("../data/"+a+".txt")]
	for line in text:
		word = line.split()
		for item in word:
			if item in dic:
				dic[item]+=1
			else:
				dic[item]=1
	return normalize(dic)

def getDictNew(a):
	dic=initializeDict()
	text = [line.strip() for line in open("../data/"+a+".txt")]
	for line in text:
		word=line.split()
		item=word[-1]
		if item in dic:
			dic[item]+=1
		else:
			dic[item]=1
	return normalize(dic)	
def getALH(dic1, dic2):
	l=0.0
	for item in dic2:
		l+=float(dic2[item])*log2(float(dic1[item]))
	return l



#dic1=getDict("train")
#dic2=getDict("test")
#q11=getALH(dic1, dic1)
#print q11
#print math.pow(2, -q11)
#q12=getALH(dic1, dic2)
#print q12
#print math.pow(2, -q12)
dic3=getDictNew("trainBB")
dic4=getDictNew("testBB")
q3=getALH(dic3, dic3)
print q3
print math.pow(2, -q3)
q4=getALH(dic3, dic4)
print q4
print math.pow(2, -q4)
