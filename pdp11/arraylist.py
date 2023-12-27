from math import *
def panjang(data):
	count=0
	if data==None:
		return count
	else:
		for i in data:
			count+=1
		return count

def bacatabelint():
	d=list(map(int(input)))
	if panjang(d)>20:
		d=d[:20]
	return d
def bacatabelfloat():
	f=list(map(float(input)))
	if panjang(f)>20:
		f=f[:20]
	return f
def bacatabelchar():
	c=list(map(char(input)))
	if panjang(c)>20:
		c=c[:20]
	return c
def tulistabeldata(data):
	l=panjang(data)
	if l<0:
		print ('{}',end='')
	else:
		print('{',end='')
		''
		for i in data:
			#if i<l-1:
			print('{}'.format(i),'',end='')
			'''else:
				print(i,end='')
				break'''
		print("}",end='')

def carielm(data,elm):
	found=None
	for e in data:
		if e == elm:
			found=e
	return found

def cariidxdata(data,elm):
	found=None
	for i in range(panjang(data)):
		if data [i]==elm:
			found=i
			break
	return found

def caribol(data,elm):
	found=False
	for i in range(panjang(data)):
		if data [i] == elm:
			found=True
			break
	return found



