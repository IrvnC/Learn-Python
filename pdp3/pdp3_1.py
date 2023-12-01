from sys import argv

def main():
	if len(argv)<1 or len(argv)>2 :
		print("usage: python pdp3_1 <arg_list+>")
	else:
		data=list(map(int, argv[1].split(',')))
		#[35,23,76,45,50,10,15,25,4,17]
		mini= 999999
		maxi= -999999
		sumData = 0
		jum=0
		for bil in data:
			sumData+=bil
			jum+=1
			if mini>bil:
				mini=bil
			if maxi<bil:
				maxi=bil
		print("Nilai Minimum : {}".format(mini))
		print("Nilai Maximum : {}".format(maxi))
		print("Nilai Rerata  : {}".format(sumData/jum))
if __name__ == '__main__':
	main()