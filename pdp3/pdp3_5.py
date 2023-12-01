from sys import argv
def main():

	if len(argv)<1 or len(argv)>3 :
		print("usage: python pdp3_2 <arg_list+>")
	else:
		data=list(map(float, argv[1].split(",")))
		phi=3.14
		r1=data[0]
		r2=data[1]
		l1=phi*r1*r1
		l2=phi*r2*r2
		selisih=l1-l2
	print("Luas L1, r= {} : {}".format(r1,l1))
	print("Luas L2, r= {} : {}".format(r2,l2))
	print("selisih l1-l2 : {}".format(selisih))

if __name__ == '__main__':
	main()