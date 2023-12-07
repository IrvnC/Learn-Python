def main():

	n=int(input("Input a number: "))
	i=0
	for i in range(1,11,1):
		print("{} x {}".format(i,n) + " = ",n*i)
   
if __name__ == '__main__':
	main()
