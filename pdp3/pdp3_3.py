from sys import argv
def main():

	if len(argv)<1 or len(argv)>3 :
		print("usage: python pdp3_3 <arg_list+>")
	else:
		data=list(map(float, argv[1].split()))
		a=data[0]
		t=data[0]
		l=(a*t)/2

	print("Luas segitiga dengan alas {} dan tinggi {} adalah {}".format(a,t,l))

if __name__ == '__main__':
	main()