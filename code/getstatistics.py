import sys

text = [line.strip() for line in open("../train.txt")]
dic={}
for line in text:
	word=line.split(" ")
	for item in word:
		if item in dic:
			dic[item]+=1
		else:
			dic[item]=1
items=[]
for item in dic:
	items.append(item)
items=sorted(items)
for item in items:
	print item
