def main():

	minim=None
	maxim=None
	n=None
	while True:
		n=[int(x) for x in input("Masukkan nilai : ").split()]
		if n[0]==-99:
			break
		else:
			if maxim is None or maxim<n:
				maxim = n
			if minim is None or minim>n:
				minim = n
			print("{}".format(n))
	print("maxim : {}".format(maxim))
	print("minim : {}".format(minim))
		
if __name__ == '__main__':
	main()