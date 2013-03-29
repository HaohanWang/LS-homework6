import sys
import math

def log2(m):
	if m==0:
		return 0.0
	else:
		return math.log(m,2)
def entropy(dic):
	e=0.0
	s=0.0
	for item in dic:
		s+=dic[item]
	for item in dic:
		p=float(dic[item])/float(s)
		e-=p*log2(p)
	return e	
