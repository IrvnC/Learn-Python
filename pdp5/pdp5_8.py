def main():
	i=0
	n=int(input("Input bil :"))
	while n!=9999:
		print(n)
		i+=1
		n=int(input("Input bil :"))
	print("Jumlah input bil : {}".format(i))
if __name__ == '__main__':
	main()