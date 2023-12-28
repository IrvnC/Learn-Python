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

def getvaluemax(data):
	maxim=-9999
	for i in data:
		if maxim<i:
			maxim=i
		return maxim

def getindexmax(data):
	maxim=-9999
	idx=-1
	for i in range(panjang(data)):
		if maxim < data[i]:
			maxim=data[i]
			idx=i
	return idx

def countingsort(data,min,max):
	aa=[0]*(max-min+1)
	for x in data:
		aa[x-min]=aa[x-min]+1
	sorted=[]
	for x,n in enumerate(aa,min):
		for i in range(n):
			sorted=sorted+[x]
	return sorted

def countingsortmm(data,minim,maxim):
	p=panjang(data)
	size=maxim-minim+1
	count=[0]*size
	for i in range(0,p):
		count[data[i]-minim]=count[data[i]-minim]+1
	for i in range(minim,maxim):
		z=0
		for j in range(0,(count[i-minim]-1)):
			data[z]=i
			z=z+1
		return data

def selectionsort(data):
	p=panjang(data)
	for i in range(0,p):
		m=i
		for j in range(i,p):
			if data[j] < data[m]:
				m=j
		t=data[i]
		data[i]=data[m]
		data[m]=t
	return data

def insertionsort(data):
	p=panjang(data)
	for i in range (1,p):
		tmp=data[i]
		j=i
		while(j>0 and tmp<data[j-i]):
			data[j]=data[j-1]
		data[j]=tmp
	return data