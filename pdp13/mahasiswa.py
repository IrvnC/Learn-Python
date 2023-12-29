from math import *

class mahasiswa():
	def __init__(self, nim=None, nama=None, ipk=0.0):
		self.nim=nim
		self.nama=nama
		self.ipk=ipk

def panjang(m):
	count=0
	for i in m:
		count=count+1
	return count

def isempty(m):
	if m==None or (m.nim==None and m.nama==None and m.ipk==0.0):
		return True

def setnim(m,newnim):
	mh=(mahasiswa())
	mh.nim=newnim

def setnama(m,newnama):
	mh=(mahasiswa())
	mh.nama=newnama

def setipk(m,newipk):
	mh=(mahasiswa())
	mh.ipk=newipk

def getnim(m):
	return m.nim

def getnama(m):
	return m.nama

def getipk(m):
	return m.ipk

def bacadata():
	mhsw=mahasiswa()
	nim,nama,ipk=[str (x) for x in input('NIM,NAMA,IPK:').split(',')]
	mhsw.nim=nim
	mhsw.nama=nama
	mhsw.ipk=ipk
	return mhsw.nim,mhsw.nama,mhsw.ipk

def tulisdata(m):
	if m==None:
		print("Tidak ada data")
	else:
		mhsw=mahasiswa()
		mhsw.nim=m.nim
		mhsw.nama=m.nama
		mhsw.ipk=m.ipk
		print(mhsw.nim,'-',mhsw.nama,'-',mhsw.ipk)
		
def printlist(data):
	for elm in data:
		tulisdata(elm)

def sorting(m,idx):
	if idx==0:
		for i in range (panjang(m)-1):
			minim=i
			for j in range(i+1,panjang(m)):
				if m[j].nim < m[minim].nim:
					minim=j
			temp=m[i]
			m[i]=m[minim]
			m[minim]=temp

	elif idx==1:
		for i in range (panjang(m)-1):
			minim=i
			for j in range(i+1,panjang(m)):
				if m[j].nama<m[minim].nama:
					minim=j
			temp=m[i]
			m[i]=m[minim]
			m[minim]=temp

	elif idx==2:
		for i in range(panjang(m)-1):
			minus=i
			for j in range(i+1,panjang(m)):
				if m[j].ipk<m[minus].ipk:
					minus=j
			temp=m[i]
			m[i]=m[minus]
			m[minus]=temp
	else:
		print ("output tidak terdaftar")

def searching1(listm,nim_find):
	#find = m for m in listm 
	#	if m.nim==nim_find:
	#return next(find)

	idx=-1
	for i in range(panjang(listm)):
		if listm[i].nim == nim_find:
			idx=i
			break
	if idx<0:
		return None
	else:
		return listm[idx]

def searching2(listm,nim):
	idx=-1
	for i in range(panjang(listm)):
		if listm[i].nim==nim:
			idx=i
			break
	return idx





'''buat list dahulu
listmhs=list()
listmhs.append(mahasiswa('aa11','aa',17))
dst.

def tulisdata(m):
	for i in range (len(m))
	print i
	print (m[i].nama)
	print nim
	print ipk

panggil list
tulisdata(listmhs)'''
