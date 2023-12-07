def main():
	sumData=0
	n=int(input("input bil : "))
	while n!= 9999:
		print(n)
		sumData+=n
		n=int(input("Input bil :"))
	print("Jumlah : {}".format(sumData))

if __name__ == '__main__':
	main()