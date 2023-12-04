import math
def main():
	a=0
	b=0
	c=0
	x=a**2+b+c

	print("persamaan kuadrat ax^2+bx+c")
	a=list(map(int, input("masukkan 3 integer : ").split(".")))
	D=(a[1]**2)-(4*a[0]*a[2])
	if a[0]==0
		print("tidak terdefinisi")
	elif D>0:	
		x1=((-[1]+math.sqrt(D))/2*a[0])
		x1=((-[1]-math.sqrt(D))/2*a[0])
		y1=str(x1)
		y2=str(x2)
		if ((len(y1))>10 and len(y2))<10:
			print("memiliki akar kuadrat real berlainan dan rasional\nD = {}\n x1={}\n x2={}".format(D,x1,x2))
		else:
			print("memiliki akar kuadrat real berlainan dan rasional\nD = {}\n x1={}\n x2={}".format(D,x1,x2))
	elif D==0
		print("{} memiliki akar kuadrat kembar dan rasional".format(D))
	elif D<0
		print("{} memiliki akar kuadrat imajiner".format(D))
	else:
		print("input tidak valid")

if __name__ == '__main__':
	main()