def main():

	c=0
	f=0
	print("C ---> F")
	for c in range(1,101,1):
		print("{} --->".format(c), (c*9/5)+32)

if __name__ == '__main__':
	main()