import sys 
import question as q
import unigram as u
import Unigram as U
import entropy as e

udic = U.getDictNew("trainB")
uentropy=e.entropy(udic)
print uentropy
result=[]
text = [line.strip() for line in open("../data/trainB.txt")]
question=q.getDic()
for i in range(1, 505):
	print "question "+str(i)
	#data=[]
	dic1={}	
	dic2={}
	count=0
	c1=0
	c2=0
	if i in question and i!=146:
		for line in text:
			word = line.split(" ")
			sent=word[:-1]
			w=word[-1]
			#for j in range(len(word)):
			count+=1
			#data.append((sent, word[i]))
			if q.askQuestion(i, question[i], sent):
				c1+=1
				if w in dic1:
					dic1[w]+=1
				else:
					dic1[w]=1
			else:
				c2+=1
				if w in dic2:
					dic2[w]+=1
				else:
					dic2[w]=1
			#sent.append(word[j])
			#if word[j]==".":
			#	sent=[]
		e1=e.entropy(dic1)
		e2=e.entropy(dic2)
		mi=uentropy-float(c1)/float(count)*e1-float(c2)/float(count)*e2
		result.append((i, mi))
result=sorted(result, key=lambda tup:tup[1])
result.reverse()
f=open("../data/resultB.txt", 'w')
f.writelines(str(result))
f.writelines("**************")
for i in range(0, 100):
	print result[i]
	f.writelines(str(result[i])+"\n")
print "******************"
for i in range(len(result)-100, len(result)):
	print result[i]
	f.writelines(str(result[i])+"\n")			
