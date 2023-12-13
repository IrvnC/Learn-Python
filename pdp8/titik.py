import math
mp={}
def makepoint(a,b,T):
	global mp
	mp[T+"absis"]=a
	mp[T+"ordinat"]=b
	return mp
def getabsis(T):
	return mp[T+'absis']
def getordinat(T):
	return mp[T+'ordinat']
def setordinat(newx,T):
	global mp
	mp[T+'ordinat']=newx
	return mp[T+'ordinat']
def setabsis(newy,T):
	global mp
	mp[T+'absis']=newy
	return mp[T+'absis']
def bacatulis():
	p1=makepoint(2.0,2.0,'1')
	p2=makepoint(-2.0,2.0,'2')
	p3=makepoint(2.0,-2.0,'3')
	p4=makepoint(-2.0,-2.0,'4')
	print('P1: ({},{})'.format(p1['1absis'],p1['1ordinat']))
	print('P2: ({},{})'.format(p2['2absis'],p2['2ordinat']))
	print('P3: ({},{})'.format(p3['3absis'],p3['3ordinat']))
	print('P4: ({},{})'.format(p4['4absis'],p4['4ordinat']))
def addp(x1,x2,y1,y2):
	return x1+x2,y1+y2
def minp(x1,x2,y1,y2):
	return x1-x2,y1-y2
def muldot(x1,x2,y1,y2):
	return x1*x2,y1*y2
def isequal(x1,x2,y1,y2):
	return(x1==x2 and y1==y2)
def isnotequal(x1,x2,y1,y2):
	return(x1!=x2 or y1!=y2)
def isless(x1,x2,y1,y2):
	return(x1+y1<x2+y2)
def greater(x1,x2,y1,y2):
	return(x1+y1>x2+y2)
def isorigin(x,y):
	return(x==0 and y==0)
def isonsbx(x):
	return (x==0)
def isonsby(y):
	return (y==0)
def kuadran(x,y):
	if x>=0 and y>=0:
		return '1'
	elif x<0 and y>=0:
		return '2'
	elif x<0 and y<0:
		return '3'
	elif x>=0 and y<0:
		return '4'
	elif x==0 and y==0:
		return 'titik pada (0,0)'
def nextx(x,T):
	global mp
	mp[T+'absis']=x+1
	return mp[T+'absis']
def nexty(y,T):
	global mp
	mp[T+'ordinat']=y+1
	return mp[T+'ordinat']
def plusdelta(x,y,deltax,deltay,T):
	global mp
	mp[T+'absis']=x+deltax
	mp[T+'ordinat']=y+deltay
	return mp[T+'absis'],mp[T+'ordinat']
def mirrorof(x,y,sb,T):
	global mp
	if sb=='sbx':
		mp[T+'ordinat']=((-1)*y)
		return x,mp[T+'ordinat']
	if sb=='sby':
		mp[T+'absis']=((-1)*x)
		return y,mp[T+'absis']
def jarakpusat(x,y):
	return '{:.2f}'.format(math.sqrt((x**2)+(y**2)))
def jarak2t(x1,y1,x2,y2):
	return '{:.2f}'.format(math.sqrt(((x2-x1)**2)+((y2-y1)**2)))
def geser(x,y,deltax,deltay,T):
	global mp
	mp[T+'absis']=x+deltax
	mp[T+'ordinat']=y+deltay
	return mp[T+'absis'],mp[T+'ordinat']
def gesersbx(x,deltax,T):
	global mp
	mp[T+'absis']=x+deltax
	return mp[T+'absis']
def gesersby(y,deltay,T):
	global mp
	mp[T+'ordinat']=y+deltay
	return mp[T+'ordinat']
def mirrorp(x,y,sb,T):
	global mp
	if sb=='sbx':
		mp[T+'ordinat']=((-1)*y)
		return x,mp [T+'ordinat']
	elif sb=='sby':
		mp[T+'absis']=((-1)*x)
		return y,mp [T+'absis']
def putar(x,y,sudut):
	return(math.cos(sudut)*x)+(math.sin(sudut)*y),((-1)*math.sin(sudut)*x)+(math.cos(sudut)*y)
	


