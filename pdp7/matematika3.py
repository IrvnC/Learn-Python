import math
def max2(a,b):
	if a>b:
		return a,b,a
	else:
		return a,b,b

def max3(a,b,c):
	a,b,x=max2(a,b)
	if x>c:
		return a,b,c,x
	else:
		return a,b,c,c

def max4(a,b,c,d):
	a,b,c,x=max3(a,b,c)
	if x>d:
		return a,b,c,d,x
	else:
		return a,b,c,d,d

def IsGanjil(n):
	if n%2!=0:
		return n,True
	else:
		return n,False

def IsPrima(n):
	if n>1:
		for x in range(2,n):
			if n%x==0:
				return n,False
				break
			else:
				return n,True
				break
		else:
			return n,True
	return

def NumOfPrima(n):
	count = 2
	text=""
	while True:
		isprime = True
		for x in range(2,int(math.sqrt(count) + 1)):
			if count%x==0:
				isprime = False
				break
		if count>=n:
			break
		if isprime:
			text=text+str(count)+" "
		count+=1
	return n,text

def Pangkat(basis,eksp):
	pangkat=basis**eksp 
	return basis,eksp,pangkat

def SumOfN(N):
	sumData=0
	for i in range(0,N+1):
		sumData+=i
	return N,sumData

def ProductOfN (N):
	kali=1
	for num in range(1,N+1,1):
		kali = kali*num
	return N,kali

def AveSumOfN (N):
	sum=0
	for num in range(1,N+1,1):
		sum = sum+num
		average = sum/N
	return N,average

def AveProdOfN (N):
	kali=1
	for num in range(1,N+1,1):
		kali = kali*num
		average = kali/N
	return N,average

def FPB (x,y):
	if x > y:
		terkecil = y
	else:
		terkecil = x
	for i in range(1, terkecil+1):
		if((x % i == 0) and (y % i == 0)):
			fpb = i
	return x,y,fpb

def C2F (C):
	F=((9/5)*C)+32
	return C,F

def F2C (F):
	C=((5/9)*(F-32))
	return F,C

def C2R (C):
	R=(4/5)*C
	return C,R

def R2C (R):
	C=((5/4)*R)
	return R,C

def Cel2Cal(Cal):
	C=Cal+273
	return Cal,C

def Cal2Cel(C):
	Cal=C-273
	return C,Cal

def R2F(R):
	F=((9/4)*R)+32
	return R,F

def F2R(F):
	R=((4/9)*(F-32))
	return F,R