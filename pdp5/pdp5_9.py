def main():
	sumData=0
	i=1
	n=int(input("input bil : "))
	while n!=9999:
		print (n)
		sumData+=n
		i+=1
		n=int(input("input bil : "))
	print("Jumlah bil : {}".format(sumData))
	print("Jumlah input bil : {}".format(i))
	
if __name__ == '__main__':
	main()