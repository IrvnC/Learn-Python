from math import *
from Global import *

def panjang():
	global CC
	CC=START()
	count=0
	while not EOP():
		count=count+1
		CC=ADV()
	return count

def hitungvokal():
	global CC
	CC=START()
	count=0
	while not EOP():
		if CC=='a' or CC == 'A' or CC == 'i' or CC == 'I' or CC == 'u' or CC == 'U' or CC == 'e' or CC == 'E' or CC == 'o' or CC == 'O':
			count=count+1
		CC=ADV()
	return count

def hitung_a():
	global CC
	CC=START()
	counta=0
	while not EOP():
		if CC =='A' or CC=='a':
			counta=counta+1
		CC=ADV()
	return counta

def hitungAN():
	global CC
	count=0
	C1=None
	CC=START()
	C2=CC
	while not EOP():
		C1=C2
		
		C2=CC
		if C1+C2=='AN' or C1+C2=='an':
			count=count+1
		CC=ADV()
	return count

def hitungblank():
	global CC
	CC = START()
	count=0
	while not EOP():
		if CC == ' ':
			count = count + 1
		CC = ADV()
	return count

def hitungCH():
	global CC
	CC = START()
	count=0
	while not EOP():
		if CC != ' ':
			count=count+1
		CC = ADV()
	return count

def hitunghuruf():
	global CC
	CC = START()
	lowercase=0
	uppercase=0
	other=0
	low='a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
	upper='A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
	while not EOP():
		if CC in low:
			lowercase = lowercase +1
		if CC in upper:
			uppercase = uppercase + 1
		else:
			other = other + 1
		CC = ADV()
	return lowercase,uppercase,other

def START():
	global F
	global CC
	filetxt = 'pitakar.txt'
	F = open(filetxt,'r')
	if not F:
		output("error")
	CC = F.read(1)
	return CC

def ADV():
	global F
	global CC
	CC = F.read(1)
	if EOP():
		F.close()
	return CC

def EOP():
	global CC
	global MARK
	return CC == MARK

#
#