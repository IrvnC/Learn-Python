from sys import argv
def main():

	if len(argv)<1 or len(argv)>3 :
		print("usage: python pdp3_4 <arg_list+>")
	else:
		data=list(map(float, argv[1].split(",")))
		p=data[0]
		l=data[1]
		luas=p*l
	print("Luas segi empat dengan p {} dan l {} adalah {}".format(p,l,luas))

if __name__ == '__main__':
	main()