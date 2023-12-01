from sys import argv
def main():

	if len(argv)<1 or len(argv)>3 :
		print("usage: python pdp3_2 <arg_list+>")
	else:
		data=list(map(float, argv[1].split(',')))
		r=data[0]
		phi=3.14
		luas= phi*data[0]*data[0]

		print("Luas lingkaran dengan r={} adalah {}".format(r,luas))

if __name__ == '__main__':
	main()