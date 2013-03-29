import sys
import math

def getUnigram():
	text = [line.strip() for line in open("../data/train.txt")]
	dic = {}
	for line in text:
		tag = line.split(" ")
		for t in tag:
			if t in dic:
				dic[t]+=1
			else:
				dic[t]=1
	return dic

def getAvgLogLikelihood(dic):
	s = 0.0
	for item in dic:
		s+=float(dic[item])
	p=0.0
	for item in dic:
		p+=math.log(float(dic[item])/float(s), 2)
	return p/len(dic)
def getPerplexity(dic):
	s = 0.0
	for item in dic:
		s+=float(dic[item])
	p=0.0
	for item in dic:
		pro = float(dic[item])/float(s)
		p+=-pro*math.log(pro, 2)
	return math.pow(2, p)

dic = getUnigram()
s=0.0
for item in dic:
	s+=dic[item]
for item in dic:
	dic[item]=float(dic[item])/float(s)
text = [line.strip() for line in open("../data/test.txt")]
l=0.0
p=0.0
count=0
for line in text:
	word = line.split(" ")
	for item in word:
		count+=1
		a=math.log(dic[item], 2)
		l+=a
		#p+=-dic[item]*a
print l/count
#print p
#print math.pow(2, p)
#avgl=getAvgLogLikelihood(dic)
#print avgl
perp=getPerplexity(dic)
print perp
