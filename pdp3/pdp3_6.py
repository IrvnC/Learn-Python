from sys import argv

def f1(p,q):
	r1=p and q
	return r1
def f2(p,q):
	r2=not(p and q)
	return r2
def f3(p):
	r3=not(p)
	return r3
def f4(q):
	r4=not(q)
	return r4
def f5(q):
	r5=p or (not q)
	return r5
def f6(p,q):
	r6=not(p and q) 
	return r6
def f7(q):
	r7=not(p or q)
	return r7
def f8(p,q):
	if p==q:
		r8=False
	else :
		r8=True
	return r8
def f9(p,q):
	if p==q:
		r9=True
	else :
		r9=False
	return r9

def output(h):
	print("T|T = {}".format(h[0]))
	print("T|F = {}".format(h[1]))
	print("F|T = {}".format(h[2]))
	print("F|F = {}".format(h[3]))

def main():
	t = True
	f = False
	andv=[0,0,0,0]

	print("output 1 :")
	andv[0] = f1(t,t)
	andv[1] = f1(t,f)
	andv[2] = f1(f,t)
	andv[3] = f1(f,f)
	output(andv)
	
	print("output 2 :")
	andv[0] = f1(t,t)
	andv[1] = f1(t,f)
	andv[2] = f1(f,t)
	andv[3] = f1(f,f)
	output(andv)
	
	print("output 3 :")
	andv[0] = f1(t,t)
	andv[1] = f1(t,f)
	andv[2] = f1(f,t)
	andv[3] = f1(f,f)
	output(andv)
	
	print("output 4 :")
	andv[0] = f1(t,t)
	andv[1] = f1(t,f)
	andv[2] = f1(f,t)
	andv[3] = f1(f,f)
	output(andv)
	
	print("output 5 :")
	andv[0] = f1(t,t)
	andv[1] = f1(t,f)
	andv[2] = f1(f,t)
	andv[3] = f1(f,f)
	output(andv)
	
	print("output 6 :")
	andv[0] = f1(t,t)
	andv[1] = f1(t,f)
	andv[2] = f1(f,t)
	andv[3] = f1(f,f)
	output(andv)
	
	print("output 7 :")
	andv[0] = f1(t,t)
	andv[1] = f1(t,f)
	andv[2] = f1(f,t)
	andv[3] = f1(f,f)
	output(andv)
	
	print("output 8 :")
	andv[0] = f1(t,t)
	andv[1] = f1(t,f)
	andv[2] = f1(f,t)
	andv[3] = f1(f,f)
	output(andv)

	print("output 9 :")
	andv[0] = f1(t,t)
	andv[1] = f1(t,f)
	andv[2] = f1(f,t)
	andv[3] = f1(f,f)
	output(andv)
	
if __name__== '__main__' :
	main()