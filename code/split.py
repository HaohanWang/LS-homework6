import sys 
import question as q
import unigram as u
import entropy as e

udic = u.getUnigram()
uentropy=e.entropy(udic)
print uentropy
result=[]
text = [line.strip() for line in open("../data/test.txt")]
A=open("../data/testA.txt", "w")
B=open("../data/testB.txt", "w")
question=q.getDic()
i=146
print "question "+str(i)
#data=[]
dic1={}	
dic2={}
count=0
c1=0
c2=0
for line in text:
	word = line.split(" ")
	sent=[]
	for j in range(len(word)):
		count+=1
		#data.append((sent, word[i]))
		if q.askQuestion(i, question[i], sent):
			S=" ".join(sent)
			A.writelines(S+" "+word[j]+"\n")
		else:
			S=" ".join(sent)
                        B.writelines(S+" "+word[j]+"\n")
		sent.append(word[j])
		if word[j]==".":
			sent=[]
#e1=e.entropy(dic1)
#e2=e.entropy(dic2)
#mi=uentropy-float(c1)/float(count)*e1-float(c2)/float(count)*e2
#result.append((i, mi))
#result=sorted(result, key=lambda tup:tup[1])
#result.reverse()
#f=open("../data/result.txt", 'w')
#f.writelines(str(result))
#f.writelines("**************")
#for i in range(0, 100):
#	print result[i]
#	f.writelines(str(result[i])+"\n")
#print "******************"
#for i in range(len(result)-100, len(result)):
#	print result[i]
#	f.writelines(str(result[i])+"\n")			
